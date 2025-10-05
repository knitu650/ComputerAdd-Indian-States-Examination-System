-- Analytics Database Schema

CREATE TABLE IF NOT EXISTS user_analytics (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(24) NOT NULL,
    exam_id VARCHAR(24) NOT NULL,
    score DECIMAL(5, 2),
    time_taken INTEGER,
    completed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_user_id (user_id),
    INDEX idx_exam_id (exam_id),
    INDEX idx_completed_at (completed_at)
);

CREATE TABLE IF NOT EXISTS daily_stats (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL UNIQUE,
    total_exams INTEGER DEFAULT 0,
    total_users INTEGER DEFAULT 0,
    total_questions_answered INTEGER DEFAULT 0,
    average_score DECIMAL(5, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS exam_stats (
    id SERIAL PRIMARY KEY,
    exam_id VARCHAR(24) NOT NULL UNIQUE,
    total_attempts INTEGER DEFAULT 0,
    average_score DECIMAL(5, 2),
    highest_score DECIMAL(5, 2),
    lowest_score DECIMAL(5, 2),
    average_time INTEGER,
    completion_rate DECIMAL(5, 2),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
