package com.computeradd.indianstates.models;

public class IndianState {
    private String name;
    private String capital;
    private long population;
    private double area;
    private String language;
    private String code;
    private String imageUrl;
    
    public IndianState() {}
    
    public IndianState(String name, String capital, long population) {
        this.name = name;
        this.capital = capital;
        this.population = population;
    }
    
    // Getters
    public String getName() { return name; }
    public String getCapital() { return capital; }
    public long getPopulation() { return population; }
    public double getArea() { return area; }
    public String getLanguage() { return language; }
    public String getCode() { return code; }
    public String getImageUrl() { return imageUrl; }
    
    // Setters
    public void setName(String name) { this.name = name; }
    public void setCapital(String capital) { this.capital = capital; }
    public void setPopulation(long population) { this.population = population; }
    public void setArea(double area) { this.area = area; }
    public void setLanguage(String language) { this.language = language; }
    public void setCode(String code) { this.code = code; }
    public void setImageUrl(String imageUrl) { this.imageUrl = imageUrl; }
}
