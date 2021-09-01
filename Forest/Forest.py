#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 21:02:15 2020

@author: amreethrajan

Version: 2

About this version: This is a program that is aimed
towards generating forests from given degree sequences

A forest can be generated for a sequence d1,...,dn iff
1. the sum of the degrees is even
2. the sum of the degrees = 2(n-1)

This method uses these conditions to verify if a forest can 
be generated. The nodes are labelled in the non-increasing
order of their degrees. There is also a list with the visit
status of each node (initially they are all marked non-visited
                     
After this, the nodes are processed in the order of their labels.
Each node is connected to the first 'i' non-visited and 
unsaturated nodes in the list. The nodes used to saturate the 
picked node are marked as visited. The node picked next is the 
first unsaturated node in the list (regardless of their visit status)

The code terminates when all the nodes are saturated. 

"""

import networkx as nx 
import ForestFunctions as ff

class For:
    def __init__(self,n,Seq):
        self.n= n #Number of nodes
        self.DS = Seq #List of prescribed degree of sequence
        self.F= nx.empty_graph(n)
        
    def GenFor(self,n,Seq):
        self.F=ff.ForestGen(self.n,self.DS,self.F)
  
def fGUI(n,L):
    if len(L)< n:
        return False
    else:
        if ff.ForCheck(n,L): 
            print ("Forest is realizable")
            return True
        else:
            return False
            
def main():           
    n = int(input("Enter no. of nodes:"))
    lst=[]
    print("\nEnter the degrees of the",n,"nodes one by one\n")
    fsum=0
    
    for i in range(0, n):
        print("\nNode #",i,":")
        ele = int(input())
        fsum+=ele
        lst.append(ele) 
        # adding the element to a list to form degree sequence
        
    fst = For(n,lst)
    
    #If it passes the conditions of forest, forest formation will ensue  
    if ff.ForCheck(n,lst): 
        print ("Forest is realizable")
        fst.GenFor(n,lst)
    else:
        print ("Forest is not realizable")
                
if __name__ == '__main__': 
    main()
        