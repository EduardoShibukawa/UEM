package com.eduardo.shibukawa.tests;

import com.eduardo.shibukawa.entity.Vertex;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by Duh on 22/07/2016.
 */
public class VertexTest {
    @Test
    public void testCreate(){
        Vertex v = new Vertex(1,1,1);
        assertNotNull(v);
}

}