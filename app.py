
# =============================================================================
# Fixed app.py with better error handling
# =============================================================================

from flask import Flask, render_template, request, jsonify
from models import get_db_connection, create_entries_table, create_users_table
from config import HUGGING_FACE_API, FLUTTERWAVE_CONFIG
import requests
import uuid
import logging
import time

app = Flask(__name__)

# Initialize database tables
create_entries_table()
create_users_table()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_emotion(text):
    """Analyze emotion using Hugging Face API with retry logic"""
    headers = {"Authorization": f"Bearer {HUGGING_FACE_API['token']}"}
    
    # Try multiple times as HF models sometimes need warmup
    for attempt in range(3):
        try:
            response = requests.post(
                HUGGING_FACE_API['url'], 
                headers=headers, 
                json={"inputs": text},
                timeout=15
            )
            
            # Handle specific error codes
            if response.status_code == 503:
                logger.warning(f"Model loading, attempt {attempt + 1}/3")
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            elif response.status_code == 403:
                logger.error("Hugging Face API token invalid or quota exceeded")
                return "neutral", 50.0  # Fallback
            
            response.raise_for_status()
            
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                # Get the top emotion with confidence score
                top_emotion = result[0][0]
                emotion = top_emotion['label'].lower()
                confidence = round(top_emotion['score'] * 100, 1)
                
                logger.info(f"Emotion detected: {emotion} ({confidence}%)")
                return emotion, confidence
            else:
                logger.warning("Unexpected API response format")
                return "neutral", 50.0
                
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed (attempt {attempt + 1}): {e}")
            if attempt == 2:  # Last attempt
                return "neutral", 50.0
            time.sleep(1)
    
    return "neutral", 50.0  # Final fallback

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_entry():
    """Submit a new journal entry and analyze emotion"""
    try:
        text = request.form.get('text', '').strip()
        if not text:
            return jsonify({'error': 'Journal entry cannot be empty'}), 400
        
        # Analyze emotion
        emotion, confidence = analyze_emotion(text)
        
        # Store in database - Check if confidence column exists
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Try with confidence column first
        try:
            cursor.execute(
                "INSERT INTO entries (text, emotion, confidence) VALUES (%s, %s, %s)", 
                (text, emotion, confidence)
            )
        except Exception as db_error:
            if "Unknown column 'confidence'" in str(db_error):
                # Fallback to original schema without confidence
                logger.warning("Confidence column missing, using original schema")
                cursor.execute(
                    "INSERT INTO entries (text, emotion) VALUES (%s, %s)", 
                    (text, emotion)
                )
            else:
                raise db_error
        
        conn.commit()
        conn.close()
        
        return jsonify({
            'emotion': emotion,
            'confidence': confidence,
            'message': f"Emotion detected: {emotion.title()} ({confidence}%)"
        })
        
    except Exception as e:
        logger.error(f"Error submitting entry: {e}")
        return jsonify({'error': 'Failed to analyze mood'}), 500

@app.route('/entries')
def get_entries():
    """Get all journal entries for display"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        # Check if confidence column exists
        cursor.execute("DESCRIBE entries")
        columns = [row['Field'] for row in cursor.fetchall()]
        
        if 'confidence' in columns:
            cursor.execute("SELECT * FROM entries ORDER BY timestamp DESC LIMIT 50")
        else:
            cursor.execute("SELECT id, text, emotion, timestamp FROM entries ORDER BY timestamp DESC LIMIT 50")
        
        entries = cursor.fetchall()
        conn.close()
        

        for entry in entries:
            if 'confidence' not in entry:
                entry['confidence'] = 75.0  # Default confidence
            if entry.get('timestamp'):
                entry['timestamp'] = entry['timestamp'].isoformat()
        
        return jsonify(entries)
        
    except Exception as e:
        logger.error(f"Error fetching entries: {e}")
        return jsonify({'error': 'Failed to load entries'}), 500

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """Handle subscription payment via Flutterwave"""
    try:
        user_email = request.form.get('user_email', 'user@example.com')
        user_name = request.form.get('user_name', 'User')
        tx_ref = str(uuid.uuid4())
        
        # Validate Flutterwave configuration
        if not FLUTTERWAVE_CONFIG['secret_key'] or 'your-secret-key' in FLUTTERWAVE_CONFIG['secret_key']:
            logger.error("Flutterwave secret key not configured")
            return jsonify({'error': 'Payment service not configured'}), 500
        
        payload = {
            "tx_ref": tx_ref,
            "amount": "300",
            "currency": "KES",
            "redirect_url": f"http://localhost:5000/subscription-success?tx_ref={tx_ref}",
            "payment_options": "card,mobilemoney",
            "customer": {
                "email": user_email,
                "name": user_name
            },
            "customizations": {
                "title": "Mood Journal Premium Subscription",
                "description": "Monthly access to premium mood analytics and insights"
            }
        }
        
        headers = {
            "Authorization": f"Bearer {FLUTTERWAVE_CONFIG['secret_key']}",
            "Content-Type": "application/json"
        }
        
        logger.info(f"Attempting payment with tx_ref: {tx_ref}")
        
        response = requests.post(
            "https://api.flutterwave.com/v3/payments", 
            json=payload, 
            headers=headers,
            timeout=15
        )
        
        logger.info(f"Flutterwave response status: {response.status_code}")
        
        if response.status_code == 401:
            logger.error("Flutterwave authentication failed - check your secret key")
            return jsonify({'error': 'Payment authentication failed'}), 500
        
        response.raise_for_status()
        
        payment_data = response.json()
        if payment_data.get('status') == 'success':
            payment_link = payment_data['data']['link']
            return jsonify({"payment_link": payment_link})
        else:
            logger.error(f"Flutterwave error: {payment_data}")
            return jsonify({'error': 'Failed to create payment link'}), 400
            
    except Exception as e:
        logger.error(f"Subscription error: {e}")
        return jsonify({'error': 'Subscription service unavailable'}), 500

@app.route('/subscription-success')
def subscription_success():
    """Handle successful subscription callback"""
    tx_ref = request.args.get('tx_ref')
    return f"<h1>✅ Subscription Successful!</h1><p>Transaction: {tx_ref}</p>"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
