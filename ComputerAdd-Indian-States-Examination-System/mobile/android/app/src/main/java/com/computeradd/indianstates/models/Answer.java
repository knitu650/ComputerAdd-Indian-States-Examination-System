package com.computeradd.indianstates.models;

public class Answer {
    private String questionId;
    private String answer;
    private boolean isCorrect;
    private int marksObtained;
    private long timeSpent;
    
    public Answer() {}
    
    public Answer(String questionId, String answer) {
        this.questionId = questionId;
        this.answer = answer;
    }
    
    // Getters
    public String getQuestionId() { return questionId; }
    public String getAnswer() { return answer; }
    public boolean isCorrect() { return isCorrect; }
    public int getMarksObtained() { return marksObtained; }
    public long getTimeSpent() { return timeSpent; }
    
    // Setters
    public void setQuestionId(String questionId) { this.questionId = questionId; }
    public void setAnswer(String answer) { this.answer = answer; }
    public void setCorrect(boolean correct) { isCorrect = correct; }
    public void setMarksObtained(int marksObtained) { this.marksObtained = marksObtained; }
    public void setTimeSpent(long timeSpent) { this.timeSpent = timeSpent; }
}
