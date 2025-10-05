package com.computeradd.indianstates;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.Fragment;
import com.google.android.material.bottomnavigation.BottomNavigationView;

public class MainActivity extends AppCompatActivity {
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        BottomNavigationView bottomNav = findViewById(R.id.bottom_navigation);
        bottomNav.setOnItemSelectedListener(item -> {
            Fragment selectedFragment = null;
            
            switch (item.getItemId()) {
                case R.id.nav_dashboard:
                    selectedFragment = new DashboardFragment();
                    break;
                case R.id.nav_exams:
                    selectedFragment = new ExamFragment();
                    break;
                case R.id.nav_states:
                    selectedFragment = new StatesFragment();
                    break;
                case R.id.nav_profile:
                    selectedFragment = new ProfileFragment();
                    break;
            }
            
            if (selectedFragment != null) {
                getSupportFragmentManager().beginTransaction()
                    .replace(R.id.fragment_container, selectedFragment)
                    .commit();
            }
            
            return true;
        });
        
        // Load default fragment
        getSupportFragmentManager().beginTransaction()
            .replace(R.id.fragment_container, new DashboardFragment())
            .commit();
    }
}
