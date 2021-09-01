
"""
Created on Thu Feb 12 01:20:42 2021

Author: 
    amreethrajan

About the code:
    The aim of this program is to use the James Riha algorithm [1]
    as a subroutine of a program that generates all possible graphs
    for a particular degree sequence. [degree sequence checked for 
    graphicality before starting]
    
    In the James-Riha method, the nodes are picked in the increasing
    order of their node labels (the nodes are labelled according to 
    their degrees at the start)
    
    For each node picked, the other nodes are grouped into
    equivalence classes where each equivalence class has nodes of the
    same degree in it. The returned solutions from the james-riha 
    partition subroutine are then each processed. 
    
    If the solution leads to a realizable degree sequence, we recurse 
    further. Otherwise we move on to the next solution without 
    recursing further on that path.
    
    This method does not generate all the labelled graphs since there
    is a restriction on how the nodes are picked from the equivalence 
    class. There is a standard within the method which implies that
    the first 'i' nodes are picked from equivalence classes rather 
    than picking the 'i' nodes randomly. If all combinations of picking 
    the 'i' nodes were to be explored, then all labelled graphs would 
    be generated

References:
[1] James, K. R., & Riha, W. (1976). Algorithm 28 algorithm for generating 
graphs of a given partition. Computing, 16(1-2), 153-161.
    
"""

#import all the libraries that are neededimport matplotlib.pyplot as plt 
import jrExhFun as jrf

if __name__ == '__main__': 
    #receive user input for n
    n = int(input("Enter no. of nodes:"))
    DegreeList=[]
    print("\nEnter the degrees of the",n,"nodes one by one when prompted\n")
    #receive user input for DSeq
    #Once the user enters each node's degree, they're aDegreeListl appended into a list
    for i in range(0, n):
        print("\nNode #",i,":")
        ele = int(input()) 
        DegreeList.append(ele) # adding the element  
    J=jrf.JRGraph(n,DegreeList)

