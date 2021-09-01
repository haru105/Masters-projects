#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 04:02:20 2021

@author: amreethrajan

About the code: 

The algorithm traverses through the inputted degree sequence
and the righmost adjacent set is found out, based on which
the other smaller sequences are found out.

The rightmost adjacent set refers to the lowest degree nodes
that can be joined to the picked node without breaking graphicality.

Each of the smaller sets are then individually processed, which 
enables for all the possible graphs to be generated (within the scope
of this method).

The method is rejection free in nature because of the theorem 
stated in [1], which states that all the sets to the left of the
rightmost set always preserves graphicality. All the paths stemming from
the rightmost set are going to be successful as a result. 

References:

[1] "Kim,H.,Toroczkai,Z.,Erdős,P.L.,Miklós,I.,&Székely,L.A.(2009).
Degree-based graph construction."

"""

import networkx as nx
import matplotlib.pyplot as plt
import KimFunex as kf

if __name__=='__main__':
    #receive user input for n
    n = int(input("Enter no. of nodes:"))
    DegreeList=[]
    print("\nEnter the degrees of the",n,"nodes one by one when prompted\n")
    #receive user input for DSeq
    #Once the user enters each node's degree, they're all appended into a list
    for i in range(0, n):
        print("\nNode #",i,":")
        ele = int(input()) 
        DegreeList.append(ele) # adding the element  
    J=kf.KimG(n,DegreeList)
