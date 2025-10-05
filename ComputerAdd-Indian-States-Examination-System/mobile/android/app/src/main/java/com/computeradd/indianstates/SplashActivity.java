package com.computeradd.indianstates;

import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import androidx.appcompat.app.AppCompatActivity;

public class SplashActivity extends AppCompatActivity {
    
    private static final int SPLASH_DURATION = 2000;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);
        
        new Handler().postDelayed(() -> {
            // Check if user is logged in
            boolean isLoggedIn = checkLoginStatus();
            
            Intent intent;
            if (isLoggedIn) {
                intent = new Intent(SplashActivity.this, MainActivity.class);
            } else {
                intent = new Intent(SplashActivity.this, LoginActivity.class);
            }
            
            startActivity(intent);
            finish();
        }, SPLASH_DURATION);
    }
    
    private boolean checkLoginStatus() {
        // Check shared preferences for auth token
        return getSharedPreferences("app_prefs", MODE_PRIVATE)
            .getString("auth_token", null) != null;
    }
}
