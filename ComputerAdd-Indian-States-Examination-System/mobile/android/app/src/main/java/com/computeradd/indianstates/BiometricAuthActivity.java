package com.computeradd.indianstates;

import android.os.Bundle;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.biometric.BiometricPrompt;
import androidx.core.content.ContextCompat;
import java.util.concurrent.Executor;

public class BiometricAuthActivity extends AppCompatActivity {
    
    private BiometricPrompt biometricPrompt;
    private BiometricPrompt.PromptInfo promptInfo;
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_biometric);
        
        setupBiometricAuth();
        showBiometricPrompt();
    }
    
    private void setupBiometricAuth() {
        Executor executor = ContextCompat.getMainExecutor(this);
        
        biometricPrompt = new BiometricPrompt(this, executor,
            new BiometricPrompt.AuthenticationCallback() {
                @Override
                public void onAuthenticationSucceeded(
                    BiometricPrompt.AuthenticationResult result) {
                    super.onAuthenticationSucceeded(result);
                    onAuthSuccess();
                }
                
                @Override
                public void onAuthenticationFailed() {
                    super.onAuthenticationFailed();
                    Toast.makeText(BiometricAuthActivity.this,
                        "Authentication failed", Toast.LENGTH_SHORT).show();
                }
                
                @Override
                public void onAuthenticationError(int errorCode, CharSequence errString) {
                    super.onAuthenticationError(errorCode, errString);
                    Toast.makeText(BiometricAuthActivity.this,
                        "Error: " + errString, Toast.LENGTH_SHORT).show();
                }
            });
        
        promptInfo = new BiometricPrompt.PromptInfo.Builder()
            .setTitle("Biometric Authentication")
            .setSubtitle("Authenticate to continue")
            .setNegativeButtonText("Use password")
            .build();
    }
    
    private void showBiometricPrompt() {
        biometricPrompt.authenticate(promptInfo);
    }
    
    private void onAuthSuccess() {
        Toast.makeText(this, "Authentication successful", Toast.LENGTH_SHORT).show();
        // Proceed to main activity
        finish();
    }
}
