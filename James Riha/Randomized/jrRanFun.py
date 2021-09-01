#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:37:34 2021

@author: amreethrajan

About the code : 
    
    This code will contain all the functions needed to make the main 
    function to work. This will contain all the classes and codes etc..

"""
import JRsplit as jr
from operator import itemgetter
from itertools import groupby
import sys
import networkx as nx
import matplotlib.pyplot as plt
import random

Gr=nx.Graph()
#graph is declared as global since we need to be working on one graph for the 
#various recursions

def recc(DS,hub):
    global Gr
    
    #we have a separate module for the first iteration in order to 
    #make the recursion possible
    if hub==-1:
        DS1=[]
        DS1=DS
        recc(DS1,0)
        return
         
    #unzipping into degree list and node list 
    DegreeList = [x[1] for x in DS]
    NodeList= [x[0] for x in DS]
    n=len(DegreeList)
    
    #this indicates a success path
    if DegreeList==n*[0]:
        print("\nSolution found! ")
        nx.draw(Gr, with_labels=True, node_color="white",edgecolors='black', font_weight='bold')
        plt.title('Graph possibility')
        plt.show()
        sys.exit(0)
        # return 1
    
    sol=[]
    n=len(DS)
    DS2=DS
    
    NonHubNodes=[]
    #NonHubNodes indicates the nodes other than the one in focus
    for i in range(hub+1,len(DS)):
        NonHubNodes.append(DS[i])
    
    #eqEligibleNodes is the list of nodes that are capable of 
    #being grouped in the eq classes i.e the ones with degree non zero
    
    eqEligibleNodes=NonHubNodes
    zeroNodes=[]
    for i in range(0,len(NonHubNodes)):
        if NonHubNodes[i][1]==0:
            zeroNodes.append(NonHubNodes[i])
    for i in zeroNodes:
        eqEligibleNodes.remove(i)

    #now on to calculating equivalence classes
    eqc = [[x for x,y in g]
               for k,g in groupby(eqEligibleNodes,key=itemgetter(1))] 
               
    for i in range(0,len(eqc)):
        random.shuffle(eqc[i])
    sumx=len(eqEligibleNodes) 
    
    #this condition checks whether if there are enough nodes for connection
    #when this happens, we return back after establishing the path as a failed one
    if sumx < DS[hub][1]:
        print("\nxxxxxxxxxxxx\nPath Failed!\nxxxxxxxxxx\n")
        return
    
    #this covers when the node of focus happens to be saturated, basically to skip over
    elif DS[hub][1]==0:
        print("\nNode already saturated; skipping to next node ")
        DS3=[]
        DS3=DS
        return recc(DS3,hub+1)
        
    else:
        eqcLengths=[]
        for i in range(0,len(eqc)):
            eqcLengths.append(len(eqc[i]))
        hubDegree=DS[hub][1]
        n_eqc=len(eqc)
        sol=jr.funIn(hubDegree,n_eqc,eqcLengths)
        print("\n\n Equivalence classes formed: \n",eqc)
        print("Parameters for solution: ",n_eqc,hubDegree,eqcLengths)
        print("Solution: ",sol)
        sol1=sol
        random.shuffle(sol)
        print("Jumbled sol: ", sol)
        #we iterate over the different solutions we get
        #Here is where the first randomization comes in 
        #Instead of iterating through the solutions, we can 
        # go through the solutions in a randoom order and 
        # stop when we get a success 
        for i in range(0,len(sol)):
            #we store the connections in order to restore them for the recursion
            #when there's a failed path we don't want to go down on
            
            resetConnections=[]
            CurrentSol=sol[i]
            print("Solution processed: ",CurrentSol)
            #for each solution, we check the computed eq classes and 
            #compute edges accordingly 
            for j in range(0,n_eqc):        
                for k in range(0,CurrentSol[j]):               
                    Gr.add_edge(DS[hub][0],eqc[j][k])
                    print("Edge between ",DS[hub][0],"and",eqc[j][k])
                    for l in range(0,len(DS)):
                        if DS[l][0]==eqc[j][k]:
                            DS[l][1]-=1
                            DS[hub][1]-=1
                            resetConnections.append(eqc[j][k])
            DS4=[]
            DS4=DS 
            print("\n**************\nDeepening recursion\n******************")
            recc(DS4,hub+1)
            DS[hub][1]+=len(resetConnections)
            #we do a reset to make sure the different solutions 
            #are explored independently 
            for j in resetConnections:
                for k in range(0,len(DS)):
                    if j==DS[k][0]:
                        Gr.remove_edge(DS[hub][0], j)
                        DS[k][1]+=1
            

class JRGraph:
    def __init__(self,N,DegreeList):
        self.n=N
        self.DegreeList=DegreeList
        #sort through the degrees and arrange them in decreasing order
        self.DegreeList.sort(reverse=True)
        self.NodeList= []
        for i in range(1,self.n+1):
            self.NodeList.append(i)
        #make a dictionary list with the keys being the nodes and the 
        #values being the degrees
        self.DS=[]
        for i in range(0,self.n):
            self.DS.append([self.NodeList[i],self.DegreeList[i]])
        self.JRGen()

                     
    def JRGen(self):
        global Gr
        DS=self.DS
        #self.L stands for the degree sequence 
        NodeList=[x[0] for x in DS]
        Gr.add_nodes_from(NodeList)
        g=recc(DS,-1)
        
  
            
            
        




