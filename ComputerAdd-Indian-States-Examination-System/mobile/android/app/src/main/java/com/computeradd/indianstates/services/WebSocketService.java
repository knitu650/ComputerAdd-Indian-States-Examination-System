package com.computeradd.indianstates.services;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import androidx.annotation.Nullable;
import okhttp3.*;

public class WebSocketService extends Service {
    
    private WebSocket webSocket;
    private OkHttpClient client;
    private static final String WS_URL = "ws://localhost:8000/ws";
    
    @Override
    public void onCreate() {
        super.onCreate();
        client = new OkHttpClient();
        connectWebSocket();
    }
    
    private void connectWebSocket() {
        Request request = new Request.Builder()
            .url(WS_URL)
            .build();
        
        webSocket = client.newWebSocket(request, new WebSocketListener() {
            @Override
            public void onOpen(WebSocket webSocket, Response response) {
                // WebSocket connected
            }
            
            @Override
            public void onMessage(WebSocket webSocket, String text) {
                // Handle incoming message
                handleMessage(text);
            }
            
            @Override
            public void onFailure(WebSocket webSocket, Throwable t, Response response) {
                // Connection failed
                reconnect();
            }
        });
    }
    
    private void handleMessage(String message) {
        // Process WebSocket message
        // TODO: Implement message handling
    }
    
    private void reconnect() {
        // Reconnect after delay
        new android.os.Handler().postDelayed(() -> connectWebSocket(), 5000);
    }
    
    public void sendMessage(String message) {
        if (webSocket != null) {
            webSocket.send(message);
        }
    }
    
    @Override
    public void onDestroy() {
        super.onDestroy();
        if (webSocket != null) {
            webSocket.close(1000, "Service destroyed");
        }
    }
    
    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
