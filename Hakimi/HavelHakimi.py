#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created over the period 17-19 Dec, 2020

@author: asish mukhopadhyay, amreeth nagarajan

Version: 1

Description: This is an implementation of the Hakim-Havel algorithm 
for testing if a finite sequence of positive integers is graphical; that is, 
does there exists a graph whose degrees are these integers ? If true, it constructs
a graph with these vertex degrees.
The original method by hakimi saturates the node in a non increasing order of degrees and strictly
in the order that they appear in the degree sequence (i.e. increasing order of node label)
In this version, nodes of the highest degrees are prioritized, and a random node amongst them
are selected to be saturated. 
"""

#If an input sequence is graphical, this code produces the same graph on every run. 
import networkx as nx 
import matplotlib.pyplot as plt 
import myHHFunction as hh
import copy

class HHTree:
    def __init__(self,n,degSeq, G):
        self.n=n
        self.degSeq = degSeq #List of prescribed degree of sequence
        self.G=nx.Graph() 

if __name__ == '__main__':            
    n = int(input("Enter no. of nodes, return and then enter the degrees (positive integers, in non-increasing order), one per line:\n")) 
    G = nx.empty_graph(n)
    #Get list of degrees 
    degList=[]
    for i in range(0, n): 
        degValue = int(input()) 
        degList.append(degValue) # adding the element
    flag = hh.constructGraph(n, degList, G)
    if (flag ==1):
       hh.displayGraph(G)
    else:
       print ("Sequence is not graphical")
       