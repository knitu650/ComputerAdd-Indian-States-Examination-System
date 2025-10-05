package com.computeradd.indianstates.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.computeradd.indianstates.R;
import com.computeradd.indianstates.models.Question;
import java.util.List;

public class QuestionAdapter extends RecyclerView.Adapter<QuestionAdapter.QuestionViewHolder> {
    
    private List<Question> questions;
    private OnAnswerSelectedListener listener;
    
    public interface OnAnswerSelectedListener {
        void onAnswerSelected(int questionIndex, String answer);
    }
    
    public QuestionAdapter(List<Question> questions, OnAnswerSelectedListener listener) {
        this.questions = questions;
        this.listener = listener;
    }
    
    @NonNull
    @Override
    public QuestionViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
            .inflate(R.layout.item_question, parent, false);
        return new QuestionViewHolder(view);
    }
    
    @Override
    public void onBindViewHolder(@NonNull QuestionViewHolder holder, int position) {
        Question question = questions.get(position);
        holder.bind(question, position, listener);
    }
    
    @Override
    public int getItemCount() {
        return questions != null ? questions.size() : 0;
    }
    
    static class QuestionViewHolder extends RecyclerView.ViewHolder {
        TextView questionText;
        RadioGroup optionsGroup;
        
        QuestionViewHolder(@NonNull View itemView) {
            super(itemView);
            questionText = itemView.findViewById(R.id.question_text);
            optionsGroup = itemView.findViewById(R.id.options_group);
        }
        
        void bind(Question question, int position, OnAnswerSelectedListener listener) {
            questionText.setText((position + 1) + ". " + question.getQuestionText());
            
            optionsGroup.removeAllViews();
            List<String> options = question.getOptions();
            
            for (int i = 0; i < options.size(); i++) {
                RadioButton radioButton = new RadioButton(itemView.getContext());
                radioButton.setText(options.get(i));
                radioButton.setId(View.generateViewId());
                optionsGroup.addView(radioButton);
            }
            
            optionsGroup.setOnCheckedChangeListener((group, checkedId) -> {
                RadioButton selectedButton = group.findViewById(checkedId);
                if (selectedButton != null && listener != null) {
                    listener.onAnswerSelected(position, selectedButton.getText().toString());
                }
            });
        }
    }
}
