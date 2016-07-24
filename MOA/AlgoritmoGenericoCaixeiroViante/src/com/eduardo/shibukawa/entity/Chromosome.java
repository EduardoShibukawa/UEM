package com.eduardo.shibukawa.entity;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

/**
 * Created by Duh on 22/07/2016.
 */
public class Chromosome {
    private ArrayList<Vertex> genes;
    private Double fitness;

    public Chromosome(ArrayList<Vertex> genes) {
        this.genes = genes;
        this.fitness = 0.00;
    }

    public void shuffle(){
        Collections.shuffle(genes);
    }

    public void evaluate(){
        this.fitness = 0.00;
    }

    @Override
    public String toString() {
        return Arrays.toString(this.genes.toArray());
    }
}
