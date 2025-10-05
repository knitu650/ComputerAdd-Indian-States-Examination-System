package com.computeradd.indianstates.models;

import java.util.List;

public class Question {
    private String id;
    private String questionText;
    private String type;
    private List<String> options;
    private String correctAnswer;
    private int marks;
    private String difficulty;
    private String state;
    private String imageUrl;
    
    public Question() {}
    
    // Getters
    public String getId() { return id; }
    public String getQuestionText() { return questionText; }
    public String getType() { return type; }
    public List<String> getOptions() { return options; }
    public String getCorrectAnswer() { return correctAnswer; }
    public int getMarks() { return marks; }
    public String getDifficulty() { return difficulty; }
    public String getState() { return state; }
    public String getImageUrl() { return imageUrl; }
    
    // Setters
    public void setId(String id) { this.id = id; }
    public void setQuestionText(String questionText) { this.questionText = questionText; }
    public void setType(String type) { this.type = type; }
    public void setOptions(List<String> options) { this.options = options; }
    public void setCorrectAnswer(String correctAnswer) { this.correctAnswer = correctAnswer; }
    public void setMarks(int marks) { this.marks = marks; }
    public void setDifficulty(String difficulty) { this.difficulty = difficulty; }
    public void setState(String state) { this.state = state; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }
}
