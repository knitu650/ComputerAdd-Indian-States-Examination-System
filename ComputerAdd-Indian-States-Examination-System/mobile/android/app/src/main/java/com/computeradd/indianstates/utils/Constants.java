package com.computeradd.indianstates.utils;

public class Constants {
    
    // API URLs
    public static final String BASE_URL = "http://localhost:8000/api/v1";
    public static final String WS_URL = "ws://localhost:8000/ws";
    
    // SharedPreferences Keys
    public static final String PREF_NAME = "IndianStatesExamPrefs";
    public static final String KEY_AUTH_TOKEN = "auth_token";
    public static final String KEY_USER_ID = "user_id";
    public static final String KEY_USER_EMAIL = "user_email";
    
    // Request Codes
    public static final int REQUEST_CAMERA = 100;
    public static final int REQUEST_STORAGE = 101;
    public static final int REQUEST_BIOMETRIC = 102;
    
    // Exam Constants
    public static final int AUTO_SAVE_INTERVAL = 30000; // 30 seconds
    public static final int WARNING_TIME = 300000; // 5 minutes
    
    // Database
    public static final String DB_NAME = "indian_states_exam.db";
    public static final int DB_VERSION = 1;
}
