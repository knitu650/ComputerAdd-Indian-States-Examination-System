package com.computeradd.indianstates.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import com.computeradd.indianstates.R;

public class ProfileFragment extends Fragment {
    
    private TextView nameText;
    private TextView emailText;
    private Button logoutButton;
    
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                            @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_profile, container, false);
        
        nameText = view.findViewById(R.id.profile_name);
        emailText = view.findViewById(R.id.profile_email);
        logoutButton = view.findViewById(R.id.logout_button);
        
        loadProfile();
        
        logoutButton.setOnClickListener(v -> handleLogout());
        
        return view;
    }
    
    private void loadProfile() {
        // TODO: Load user profile from preferences/API
        nameText.setText("John Doe");
        emailText.setText("john.doe@example.com");
    }
    
    private void handleLogout() {
        // TODO: Clear session and navigate to login
    }
}
