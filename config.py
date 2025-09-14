import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_required_env(key, description=""):
    """Get required environment variable or exit with error"""
    value = os.getenv(key)
    if not value:
        print(f"❌ ERROR: Missing required environment variable: {key}")
        if description:
            print(f"   Description: {description}")
        print(f"   Please set {key} in your .env file or environment")
        sys.exit(1)
    return value

# Database Configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': get_required_env('DB_PASSWORD', 'Database password'),
    'database': os.getenv('DB_NAME', 'mood_journal'),
    'charset': 'utf8mb4',
    'autocommit': False
}

# Hugging Face API Configuration
HUGGING_FACE_API = {
    'url': 'https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base',
    'token': get_required_env('HUGGING_FACE_TOKEN', 'Hugging Face API token')
}

# Flutterwave Payment Configuration
FLUTTERWAVE_CONFIG = {
    'public_key': get_required_env('FLUTTERWAVE_PUBLIC_KEY', 'Flutterwave public key'),
    'secret_key': get_required_env('FLUTTERWAVE_SECRET_KEY', 'Flutterwave secret key'),
    'encryption_key': get_required_env('FLUTTERWAVE_ENCRYPTION_KEY', 'Flutterwave encryption key'),
    'webhook_hash': os.getenv('FLUTTERWAVE_WEBHOOK_HASH', '')  # Optional
}

# Application Configuration
APP_CONFIG = {
    'subscription_amount': int(os.getenv('SUBSCRIPTION_AMOUNT', '300')),
    'currency': os.getenv('CURRENCY', 'KES'),
    'subscription_duration_days': int(os.getenv('SUBSCRIPTION_DAYS', '30')),
    'debug': os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
}
