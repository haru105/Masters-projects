#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 01:09:53 2021

@author: amreethrajan

About the code: 
 
A split graph is a graph in which the vertex set can be divided into
a clique and a set of independent nodes.
The algorithm traverses through the inputted degree sequence
and first checks if it satisfies the conditions to be a split graph
Once that is done, we generate the split graph by picking a m value 
i.e. the highest value of i for which di≤ i-1. 
This is followed by a function that checks if a degree sequence can 
be realized as a split graph 

"""
import splitFunV1 as sf

if __name__=='__main__':
    #receive user input for n
    n = int(input("Enter no. of nodes:"))
    L=[]

    print("\nEnter the degrees of the",n,"nodes one by one when prompted\n")
    #receive user input for DSeq
    #Once the user enters each node's degree, they're all appended into a list
    for i in range(0, n):
        print("\nNode #",i+1,":")
        ele = int(input()) 
        L.append(ele) # adding the element  
    J=sf.SplitG(n,L)
