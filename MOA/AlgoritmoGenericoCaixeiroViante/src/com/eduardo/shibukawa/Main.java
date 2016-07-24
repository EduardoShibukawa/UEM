package com.eduardo.shibukawa;

import com.eduardo.shibukawa.entity.Chromosome;
import com.eduardo.shibukawa.entity.TSPGenericAlgorithmSolver;
import com.eduardo.shibukawa.entity.Vertex;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        ArrayList<Vertex> input = new ArrayList<Vertex>();
        TSPGenericAlgorithmSolver solver = new TSPGenericAlgorithmSolver();
        int i, n;
        double x, y;

        n = reader.nextInt();
        for (i = 0; i < n; i++){
            x = reader.nextDouble();
            y = reader.nextDouble();

            Vertex v = new Vertex(i, x, y);
            input.add(v);
        }
        System.out.println(input.toString());
        Chromosome best = solver.Solve(input);
        System.out.println(best.toString());
    }
}
