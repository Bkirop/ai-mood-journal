import mysql.connector
from config import DB_CONFIG
import logging

logger = logging.getLogger(__name__)

def get_db_connection():
    """Create a database connection with error handling"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except mysql.connector.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise

def create_users_table():
    """Create users table if it doesn't exist"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                is_subscribed BOOLEAN DEFAULT FALSE,
                subscription_end_date DATETIME NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        logger.info("Users table created/verified successfully")
    except mysql.connector.Error as e:
        logger.error(f"Error creating users table: {e}")
        raise
    finally:
        cursor.close()
        conn.close()

def create_entries_table():
    """Create entries table with improved structure"""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT DEFAULT 1,
                text TEXT NOT NULL,
                emotion VARCHAR(50) NOT NULL,
                confidence DECIMAL(5,2) DEFAULT 0.00,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                INDEX idx_timestamp (timestamp),
                INDEX idx_emotion (emotion)
            )
        """)
        conn.commit()
        logger.info("Entries table created/verified successfully")
    except mysql.connector.Error as e:
        logger.error(f"Error creating entries table: {e}")
        raise
    finally:
        cursor.close()
        conn.close()