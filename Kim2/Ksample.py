#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:46:42 2021

@author: amreethrajan

About the code: 
    
The algorithm receives a degree sequence, based on which a graph 
is generated at random. The sampling is said to be biased in the paper. 
The highest degree node is assigned as the hub at the start and after
every main step.

The hub node is saturated by connecting it to a node picked randomly 
from an allowed set. 

For each hub node saturation, the first connection is going to be rejection
free which means that the allowed set for the hub node has all the nodes.
For the connections onwards, the allowed set calculation gets complex.

The aim is to find a point of failure amongst the rest of the nodes.
[1] states that all the nodes to the right of the failure point, will also 
result in a failure.

Let 'i' be the degree to be saturated.[1] states that the leftmost 'i' 
nodes will not result in a failure. They are by default a part of the 
allowed set. This means that we only need to process the nodes to the 
right of this set. 

This set is then searched for a failure node using a binary search 
technique. Once the allowed set is finalized, the hub node is joined 
to a node picked randomly from this set.

This gets repeated until the hub node is saturated; and the entire process
is followed for the other nodes until ALL the nodes get saturated 

References:
    [1] "Del Genio, C. I., Kim, H., Toroczkai, Z., & Bassler, 
    K. E. (2010). Efficient and exact sampling of simple graphs 
    with given arbitrary degree sequence. PloS one, 5(4), e10012."

"""
import Ksamplefun as ksf

if __name__=='__main__':
    #receive user input for n
    n = int(input("Enter no. of nodes:"))
    DegList=[]
    print("\nEnter the degrees of the",n,"nodes one by one when prompted\n")
    #receive user input for DSeq
    #Once the user enters each node's degree, they're all appended into a list
    for i in range(0, n):
        print("\nNode #",i,":")
        ele = int(input()) 
        DegList.append(ele) 
        # adding the element to the degree list 
    #invoking the function
    J=ksf.KimG(n,DegList)
