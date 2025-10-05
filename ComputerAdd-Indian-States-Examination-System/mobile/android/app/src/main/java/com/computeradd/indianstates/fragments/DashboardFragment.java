package com.computeradd.indianstates.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import com.computeradd.indianstates.R;

public class DashboardFragment extends Fragment {
    
    private TextView welcomeText;
    private TextView statsText;
    
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                            @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_dashboard, container, false);
        
        welcomeText = view.findViewById(R.id.welcome_text);
        statsText = view.findViewById(R.id.stats_text);
        
        loadDashboardData();
        
        return view;
    }
    
    private void loadDashboardData() {
        // TODO: Load user stats from API
        welcomeText.setText("Welcome back!");
        statsText.setText("15 Exams Taken | 85% Avg Score");
    }
}
