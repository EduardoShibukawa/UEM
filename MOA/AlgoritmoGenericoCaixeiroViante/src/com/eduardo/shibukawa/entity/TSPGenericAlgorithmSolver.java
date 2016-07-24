package com.eduardo.shibukawa.entity;

import com.eduardo.shibukawa.interfaces.IChromosomeBreeder;
import com.eduardo.shibukawa.interfaces.IChromosomeMutator;
import com.eduardo.shibukawa.interfaces.IPopulationSelector;
import com.eduardo.shibukawa.interfaces.ITSPAlgorithmSolver;

import java.util.ArrayList;

/**
 * Created by Duh on 22/07/2016.
 */
public class TSPGenericAlgorithmSolver implements ITSPAlgorithmSolver {
    private ArrayList<Vertex> input;
    private Population population;
    private int generation;

    private IPopulationSelector selector;
    private IChromosomeBreeder breeder;
    private IChromosomeMutator mutator;

    public TSPGenericAlgorithmSolver() {
        this.population = new Population(50);
        this.selector = new TournamentSelector();
    }

    public Chromosome Solve(ArrayList<Vertex> input){
        this.input = input;
        this.generation = 0;

        this.generateInitialPopulation();
        while (this.Continue()){
            this.evaluate();
            this.select();
            this.crossOver();
            this.mutate();
            this.update();
        }

        return population.BestChromosome();
    }

    private void generateInitialPopulation() {
        this.population.generateShuffledPopulation(input);
    }

    private Boolean Continue(){
        this.generation += 1;
        return this.generation <= 100;
    }

    private void evaluate(){
        this.population.evaluate();
    }

    private void select(){
        this.selector.select(this.population);
    }

    private void crossOver(){
        this.breeder.breed(null,null);
    }

    private void mutate(){
        this.mutator.mutate(null);
    }

    private void update(){
    }
}
