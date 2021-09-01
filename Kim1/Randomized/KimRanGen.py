7#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 04:02:20 2021

@author: amreethrajan

About the code: The following code is based on the algorithm
enlisted in the paper- 
"Kim,H.,Toroczkai,Z.,Erdős,P.L.,Miklós,I.,&Székely,L.A.(2009).
Degree-based graph construction."

The algorithm is a modified version of the exhaustive kim's
algorithm to make it sample rather than exhaustively traverses.
The inputted degree sequence is traversed and the righmost adjacent
set is calculated. In the exhaustive method, all the other smaller 
sequences are found out. In this method, instead of generating all the 
smalller sets, we generate a single random small set. This set is then 
pursued to eventually generate a single graph.

This method needs no backtracking because of the rejection free nature
of the exhaustive method.
  
"""
import KimRanFun as kf

if __name__=='__main__':
    # receive user input for n
    n = int(input("Enter no. of nodes:"))
    DegList=[]
    print("\nEnter the degrees of the",n,"nodes one by one when prompted\n")
    #receive user input for DSeq
    #Once the user enters each node's degree, they're all appended into a list
    for i in range(0, n):
        print("\nNode #",i,":")
        element = int(input()) 
        DegList.append(element) # adding the element  
    J=kf.KimG(n,DegList)

