package com.eduardo.shibukawa.entity;

import java.util.ArrayList;

/**
 * Created by Duh on 22/07/2016.
 */
public class Population {
    private ArrayList<Chromosome> chromosomes;
    private int size;

    public Population(int size) {
        this.chromosomes = new ArrayList<>();
        this.size = size;
    }

    public void evaluate(){
        for (Chromosome c : this.chromosomes){
            c.evaluate();
        }
    }

    public Chromosome BestChromosome(){
        return chromosomes.get(0);
    }

    public void generateShuffledPopulation(ArrayList<Vertex> genes){
        this.chromosomes.clear();
        for (int i = 0; i < this.size; i++){
            Chromosome c = new Chromosome(genes);
            c.shuffle();
            this.chromosomes.add(c);
        }
    }
}
