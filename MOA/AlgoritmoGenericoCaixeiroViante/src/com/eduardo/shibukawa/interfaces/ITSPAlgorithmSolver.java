package com.eduardo.shibukawa.interfaces;

import com.eduardo.shibukawa.entity.Chromosome;
import com.eduardo.shibukawa.entity.Vertex;

import java.util.ArrayList;

/**
 * Created by Duh on 22/07/2016.
 */
public interface ITSPAlgorithmSolver {
    Chromosome Solve(ArrayList<Vertex> input);
}
