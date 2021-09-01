
"""
Created on Thu Feb 12 01:20:42 2021

Author: 
    amreethrajan

About the code:
    This is a modified version of the exhaustive james-riha algorithm
    The previously  exhaustive algorithm is randomized in two ways
        1. A single solution is randomly picked from the space of the 
            different solutions that are returned by the j-r subroutine
        2. Within each equivalence class, the nodes are picked randomly
            instead of in order of their labels.
            
    When a randomly picked solution leads to a non realizable degree 
    sequence (implying a failure), we backtrack one step to randomly 
    pick a different solution.
    
    When the randomly picked solution leads to a realizable degree 
    sequence, then we recurse deeper. The process stops when all the 
    nodes are saturated.
            
"""

#import all the libraries that are needed
import jrRanFun as jrf

if __name__ == '__main__': 
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
    J=jrf.JRGraph(n,DegreeList)

