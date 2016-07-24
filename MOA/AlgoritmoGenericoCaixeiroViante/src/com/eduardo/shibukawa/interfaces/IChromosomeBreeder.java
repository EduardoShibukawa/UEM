package com.eduardo.shibukawa.interfaces;

import com.eduardo.shibukawa.entity.Chromosome;

/**
 * Created by Duh on 24/07/2016.
 */
public interface IChromosomeBreeder {
    Chromosome breed(Chromosome c1, Chromosome c2);
}
