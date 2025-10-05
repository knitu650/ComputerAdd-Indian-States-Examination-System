package com.computeradd.indianstates.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.computeradd.indianstates.R;
import com.computeradd.indianstates.models.Exam;
import java.util.List;

public class ExamAdapter extends RecyclerView.Adapter<ExamAdapter.ExamViewHolder> {
    
    private List<Exam> exams;
    private OnExamClickListener listener;
    
    public interface OnExamClickListener {
        void onExamClick(Exam exam);
    }
    
    public ExamAdapter(List<Exam> exams, OnExamClickListener listener) {
        this.exams = exams;
        this.listener = listener;
    }
    
    @NonNull
    @Override
    public ExamViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
            .inflate(R.layout.item_exam, parent, false);
        return new ExamViewHolder(view);
    }
    
    @Override
    public void onBindViewHolder(@NonNull ExamViewHolder holder, int position) {
        Exam exam = exams.get(position);
        holder.bind(exam, listener);
    }
    
    @Override
    public int getItemCount() {
        return exams != null ? exams.size() : 0;
    }
    
    static class ExamViewHolder extends RecyclerView.ViewHolder {
        TextView titleText;
        TextView descriptionText;
        TextView durationText;
        TextView questionsText;
        
        ExamViewHolder(@NonNull View itemView) {
            super(itemView);
            titleText = itemView.findViewById(R.id.exam_title);
            descriptionText = itemView.findViewById(R.id.exam_description);
            durationText = itemView.findViewById(R.id.exam_duration);
            questionsText = itemView.findViewById(R.id.exam_questions);
        }
        
        void bind(Exam exam, OnExamClickListener listener) {
            titleText.setText(exam.getTitle());
            descriptionText.setText(exam.getDescription());
            durationText.setText(exam.getDuration() + " min");
            questionsText.setText(exam.getTotalQuestions() + " questions");
            
            itemView.setOnClickListener(v -> {
                if (listener != null) {
                    listener.onExamClick(exam);
                }
            });
        }
    }
}
