package com.eduardo.shibukawa.entity;

/**
 * Created by Duh on 21/07/2016.
 */
public class Vertex {
    private int id;
    private double x;
    private double y;
    private double fitness;

    public Vertex(int id, double x, double y){
        this.id = id;
        this.x = x;
        this.y = y;
        this.fitness = 0;
    }

    @Override
    public String toString() {
        return String.format("{id:%1$d x:%2$,.2f y:%3$,.2f}", this.id, this.x, this.y);
    }
}
