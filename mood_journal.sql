-- Create the database
CREATE DATABASE IF NOT EXISTS mood_journal;
USE mood_journal;

-- Users table
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL,
  is_subscribed BOOLEAN DEFAULT FALSE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Journal entries table
CREATE TABLE IF NOT EXISTS entries (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  text TEXT,
  emotion VARCHAR(50),
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Streak tokens table
CREATE TABLE IF NOT EXISTS streak_tokens (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  token_count INT DEFAULT 0,
  FOREIGN KEY (user_id) REFERENCES users(id)
);
