
# 🧠 AI-Powered Mood Journal

![Mood Journal Banner](https://img.shields.io/badge/AI-Powered-blue) ![Flask](https://img.shields.io/badge/Flask-Framework-green) ![MySQL](https://img.shields.io/badge/MySQL-Database-orange) ![Chart.js](https://img.shields.io/badge/Chart.js-Visualization-red)

An intelligent mood tracking application that uses AI to analyze your emotions and provides beautiful visualizations of your mental health journey.

## ✨ Features

- 🤖 **AI-Powered Emotion Detection** - Uses Hugging Face's emotion analysis model
- 📊 **Interactive Charts** - Beautiful mood trends and distribution charts
- 💳 **Premium Subscriptions** - Flutterwave payment integration for KES market
- 📱 **Responsive Design** - Works perfectly on desktop and mobile
- 🔒 **Secure Database** - MySQL with proper data structure
- 📈 **Confidence Scores** - Shows AI confidence levels (e.g., "happy: 85%")
- 🎯 **Real-time Analytics** - Live mood statistics and trends

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Chart.js
- **Backend**: Python Flask
- **Database**: MySQL
- **AI**: Hugging Face Transformers API
- **Payments**: Flutterwave API
- **Styling**: Modern CSS with gradients and animations

## 📁 Project Structure

```
mood-journal/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── models.py             # Database models and functions
├── templates/
│   └── index.html        # Frontend with charts
├── mood_journal.sql      # Database schema
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables 
└── README.md            # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- MySQL 8.0+
- Hugging Face account (free)
- Flutterwave account (for payments)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bkirop/ai-mood-journal.git
   cd ai-mood-journal
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MySQL database**
   ```bash
   mysql -u root -p < mood_journal.sql
   ```

4. **Configure environment variables**
   Create a `.env` file:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=Brian1@Kibu
   DB_NAME=mood_journal
   HUGGING_FACE_TOKEN=h****KBJW
   FLUTTERWAVE_SECRET_KEY=******
   FLUTTERWAVE_PUBLIC_KEY=FLWPUBK-43*******97-X
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000`

## 🔧 Configuration

### Hugging Face Setup
1. Go to [Hugging Face](https://huggingface.co/settings/tokens)

### Flutterwave Setup
1. Create account at [Flutterwave](https://flutterwave.com)
2. Get your API keys from the dashboard
3. Added keys to  `.env` file

### Database Setup
```sql
-- Create database
CREATE DATABASE mood_journal;

-- Add confidence column if upgrading
ALTER TABLE entries ADD COLUMN confidence DECIMAL(5,2) DEFAULT 75.00;
```

## 📊 How It Works

1. **User Input**: User writes a journal entry in the web form
2. **AI Analysis**: Text is sent to Hugging Face emotion detection model
3. **Database Storage**: Entry and emotion data stored in MySQL
4. **Visualization**: Chart.js displays mood trends and distribution
5. **Premium Features**: Flutterwave handles subscription payments

## 🎨 API Endpoints

- `GET /` - Main dashboard
- `POST /submit` - Submit journal entry for analysis
- `GET /entries` - Retrieve all journal entries
- `POST /subscribe` - Handle premium subscriptions
- `GET /subscription-success` - Payment success callback
## 📈 Future Enhancements

- [ ] User authentication and registration
- [ ] Export mood data to PDF reports
- [ ] Mood prediction using historical data
- [ ] Integration with wearable devices
- [ ] Mood-based music recommendations
- [ ] Group therapy features
- [ ] Mobile app version

## 🌐 Deployment Options

### GitHub Pages (Static Demo)
1. Create static version without Flask backend
2. Used mock data for demonstration
3. Enabled GitHub Pages in repository settings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 Requirements

```txt
Flask==2.3.3
mysql-connector-python==8.1.0
requests==2.31.0
python-dotenv==1.0.0
```


## 🎯 Demo

**Live Demo**: [https://Bkrop.github.io/ai-mood-journal](https://bkirop.github.io/ai-mood-journal/)

**Screenshots**:
- Dashboard with emotion analysis
- Interactive mood charts
- Premium subscription flow

## 📱 Mobile Responsiveness

The application is fully responsive and works seamlessly on:
- 📱 Mobile phones (iOS/Android)
- 📱 Tablets
- 💻 Desktop computers
- 🖥️ Large screens

## 🧪 Testing

```bash
# Test emotion analysis
curl -X POST http://localhost:5000/submit \
  -F "text=I'm feeling amazing today!"

# Test entries retrieval
curl http://localhost:5000/entries
```

## 📊 Database Schema

```sql
-- Users table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    is_subscribed BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Entries table
CREATE TABLE entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT DEFAULT 1,
    text TEXT NOT NULL,
    emotion VARCHAR(50) NOT NULL,
    confidence DECIMAL(5,2) DEFAULT 75.00,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## 🎨 Design Philosophy

- **Modern UI/UX** with gradient backgrounds and smooth animations
- **Accessibility-first** design with proper ARIA labels
- **Mobile-responsive** layout that works on all devices
- **Data visualization** using Chart.js for interactive mood tracking
- **Performance-optimized** with efficient database queries

## 🔍 AI Model Details

**Emotion Detection Model**: `j-hartmann/emotion-english-distilroberta-base`
- **Input**: Natural language text
- **Output**: 7 emotions (joy, sadness, anger, fear, surprise, disgust, neutral)
- **Confidence**: Percentage score for prediction accuracy
- **Languages**: English (primary), multi-language support available

## 💡 Tips for Better Emotion Detection

- Write detailed entries (50+ words work best)
- Use descriptive emotional language
- Include context about your day
- Be honest about your feelings

## 🆘 Support

- 📧 Email: briankirop@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/Bkirop/ai-mood-journal/issues)
- 📚 Docs: [Project Wiki](https://github.com/Bkirop/ai-mood-journal/wiki)
- 💬 Discussions: [GitHub Discussions](https://github.com/Bkirop/ai-mood-journal/discussions)

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co) for emotion detection models
- [Flutterwave](https://flutterwave.com) for payment processing in Kenya
- [Chart.js](https://chartjs.org) for beautiful visualizations
- [Flask](https://flask.palletsprojects.com) for the web framework
- [MySQL](https://mysql.com) for reliable data storage

## 🌟 Star History

If this project helped you, please give it a ⭐ on GitHub!

---

**Built with ❤️ in Kenya** | **Powered by AI** | **Open Source**
=======
# ai-mood-journal
AI-powered emotion tracker with sentiment analysis and mood visualizations

