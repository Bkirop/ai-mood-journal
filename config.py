import os

# Database Configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'Brian1@Kibu'),
    'database': os.getenv('DB_NAME', 'mood_journal'),
    'charset': 'utf8mb4',
    'autocommit': False
}

# Hugging Face API Configuration
HUGGING_FACE_API = {
    'url': 'https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base',
    'token': os.getenv('HUGGING_FACE_TOKEN', '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')
}

# Flutterwave Payment Configuration
FLUTTERWAVE_CONFIG = {
    'public_key': os.getenv('FLUTTERWAVE_PUBLIC_KEY', 'FLWPUBK-435f48c259404572356f14e4b44b7797-X'),
    'secret_key': os.getenv('FLUTTERWAVE_SECRET_KEY', '******'),
    'encryption_key': os.getenv('FLUTTERWAVE_ENCRYPTION_KEY', '******'),
    'webhook_hash': os.getenv('FLUTTERWAVE_WEBHOOK_HASH', '')
}

# Application Configuration
APP_CONFIG = {
    'subscription_amount': 300,
    'currency': 'KES',
    'subscription_duration_days': 30
}