package com.computeradd.indianstates.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.computeradd.indianstates.R;
import com.computeradd.indianstates.adapters.ExamAdapter;
import com.computeradd.indianstates.models.Exam;
import java.util.ArrayList;
import java.util.List;

public class ExamFragment extends Fragment {
    
    private RecyclerView recyclerView;
    private ExamAdapter adapter;
    
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                            @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_exam, container, false);
        
        recyclerView = view.findViewById(R.id.exams_recycler_view);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        
        loadExams();
        
        return view;
    }
    
    private void loadExams() {
        // TODO: Load exams from API
        List<Exam> exams = new ArrayList<>();
        // Sample data
        
        adapter = new ExamAdapter(exams, exam -> {
            // Handle exam click
            // Navigate to exam details
        });
        
        recyclerView.setAdapter(adapter);
    }
}
