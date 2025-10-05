package com.computeradd.indianstates.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.computeradd.indianstates.R;
import com.computeradd.indianstates.models.IndianState;
import java.util.List;

public class StateAdapter extends RecyclerView.Adapter<StateAdapter.StateViewHolder> {
    
    private List<IndianState> states;
    private OnStateClickListener listener;
    
    public interface OnStateClickListener {
        void onStateClick(IndianState state);
    }
    
    public StateAdapter(List<IndianState> states, OnStateClickListener listener) {
        this.states = states;
        this.listener = listener;
    }
    
    @NonNull
    @Override
    public StateViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
            .inflate(R.layout.item_state, parent, false);
        return new StateViewHolder(view);
    }
    
    @Override
    public void onBindViewHolder(@NonNull StateViewHolder holder, int position) {
        IndianState state = states.get(position);
        holder.bind(state, listener);
    }
    
    @Override
    public int getItemCount() {
        return states != null ? states.size() : 0;
    }
    
    static class StateViewHolder extends RecyclerView.ViewHolder {
        ImageView stateImage;
        TextView nameText;
        TextView capitalText;
        TextView populationText;
        
        StateViewHolder(@NonNull View itemView) {
            super(itemView);
            stateImage = itemView.findViewById(R.id.state_image);
            nameText = itemView.findViewById(R.id.state_name);
            capitalText = itemView.findViewById(R.id.state_capital);
            populationText = itemView.findViewById(R.id.state_population);
        }
        
        void bind(IndianState state, OnStateClickListener listener) {
            nameText.setText(state.getName());
            capitalText.setText("Capital: " + state.getCapital());
            populationText.setText("Population: " + formatPopulation(state.getPopulation()));
            
            // TODO: Load image with Glide or Picasso
            
            itemView.setOnClickListener(v -> {
                if (listener != null) {
                    listener.onStateClick(state);
                }
            });
        }
        
        private String formatPopulation(long population) {
            if (population >= 10000000) {
                return String.format("%.1fM", population / 1000000.0);
            } else if (population >= 100000) {
                return String.format("%.1fL", population / 100000.0);
            }
            return String.valueOf(population);
        }
    }
}
