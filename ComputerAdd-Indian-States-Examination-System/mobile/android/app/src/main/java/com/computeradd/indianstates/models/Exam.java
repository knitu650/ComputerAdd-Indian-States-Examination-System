package com.computeradd.indianstates.models;

import java.util.Date;
import java.util.List;

public class Exam {
    private String id;
    private String title;
    private String description;
    private int duration; // in minutes
    private int totalQuestions;
    private int totalMarks;
    private Date startDate;
    private Date endDate;
    private String difficulty;
    private List<String> states;
    private boolean isActive;
    
    public Exam() {}
    
    // Getters
    public String getId() { return id; }
    public String getTitle() { return title; }
    public String getDescription() { return description; }
    public int getDuration() { return duration; }
    public int getTotalQuestions() { return totalQuestions; }
    public int getTotalMarks() { return totalMarks; }
    public Date getStartDate() { return startDate; }
    public Date getEndDate() { return endDate; }
    public String getDifficulty() { return difficulty; }
    public List<String> getStates() { return states; }
    public boolean isActive() { return isActive; }
    
    // Setters
    public void setId(String id) { this.id = id; }
    public void setTitle(String title) { this.title = title; }
    public void setDescription(String description) { this.description = description; }
    public void setDuration(int duration) { this.duration = duration; }
    public void setTotalQuestions(int totalQuestions) { this.totalQuestions = totalQuestions; }
    public void setTotalMarks(int totalMarks) { this.totalMarks = totalMarks; }
    public void setStartDate(Date startDate) { this.startDate = startDate; }
    public void setEndDate(Date endDate) { this.endDate = endDate; }
    public void setDifficulty(String difficulty) { this.difficulty = difficulty; }
    public void setStates(List<String> states) { this.states = states; }
    public void setActive(boolean active) { isActive = active; }
}
