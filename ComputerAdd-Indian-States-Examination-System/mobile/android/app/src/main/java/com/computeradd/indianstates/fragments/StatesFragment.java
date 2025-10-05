package com.computeradd.indianstates.fragments;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.GridLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import com.computeradd.indianstates.R;
import com.computeradd.indianstates.adapters.StateAdapter;
import com.computeradd.indianstates.models.IndianState;
import java.util.ArrayList;
import java.util.List;

public class StatesFragment extends Fragment {
    
    private RecyclerView recyclerView;
    private StateAdapter adapter;
    
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                            @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_states, container, false);
        
        recyclerView = view.findViewById(R.id.states_recycler_view);
        recyclerView.setLayoutManager(new GridLayoutManager(getContext(), 2));
        
        loadStates();
        
        return view;
    }
    
    private void loadStates() {
        List<IndianState> states = new ArrayList<>();
        // TODO: Load states data
        
        adapter = new StateAdapter(states, state -> {
            // Handle state click
            // Navigate to state details
        });
        
        recyclerView.setAdapter(adapter);
    }
}
