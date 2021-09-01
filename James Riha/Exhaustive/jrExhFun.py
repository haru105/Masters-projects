#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:37:34 2021

@author: amreethrajan
About the code: 
    This code will contain all the functions needed to make the main 
    function to work. This will contain all the classes and codes etc..

"""

import JRsplit as jr
from operator import itemgetter
from itertools import groupby
import networkx as nx
import matplotlib.pyplot as plt
import copy

Gr=nx.Graph()
#graph is declared as global since we need to be working on one graph for the 
#various recursions

def recc(DS,hub):
    global Gr
    print("\n\nEntering with degree sequence ",DS)
    #we have a separate module for the first iteration in order to make the recursion possible
    if hub==-1:
        DS1=[]
        DS1=DS
        reccReturn=recc(DS1,0)
        return
    
    #unzipping into degree list and node list 
    DL = [x[1] for x in DS]
    n=len(DL)
    
    #this indicates a success path
    if DL==n*[0]:
        nx.draw(Gr, with_labels=True, node_color="white",edgecolors='black', font_weight='bold')
        plt.title('James Riha graph')
        plt.show()
        return 1
    
    sol=[]
    n=len(DS)
    NonHubNodes=DS[hub+1:]
    #NonHubNodes indicates the nodes other than the one in focus    
    #eqcEligibleNodes is the list of nodes that are capable of being grouped in the eq classes i.e the ones with degree non zero
    eqcEligibleNodes=copy.deepcopy(NonHubNodes)
    zeroNodes=[]
    for i in range(0,len(NonHubNodes)):
        if NonHubNodes[i][1]==0:
            zeroNodes.append(NonHubNodes[i])
    for i in zeroNodes:
        eqcEligibleNodes.remove(i)

    #now on to calculating equivalence classes
    eqc = [[x for x,y in g]
               for k,g in groupby(eqcEligibleNodes,key=itemgetter(1))]  
    sumx=len(eqcEligibleNodes) 
    
    #this condition checks whether if there are enough nodes for connection
    #when this happens, we return back after establishing the path as a failed one
    if sumx < DS[hub][1]:
        print("\nfailed path")
        return 0
    
    #this covers when the node of focus happens to be saturated, basically to skip over
    elif DS[hub][1]==0:
        DS2=[]
        DS2=DS
        return recc(DS2,hub+1)
        
    else:
        eqcLengths=[]
        for i in range(0,len(eqc)):
            eqcLengths.append(len(eqc[i]))
        HubDegree=DS[hub][1]
        print("Eq classes", eqc)
        
        n_eqc=len(eqc)
        sol=jr.funIn(HubDegree,n_eqc,eqcLengths)
        print("solutions:",sol)
        #we iterate over the different solutions we get
        
        for i in range(0,len(sol)):
            resetConnections=[]
            pickedSolution=sol[i]
            print("solution being processed: ",pickedSolution)
            #for each solution, we check the computed eq classes and compute edges accordingly 
            for j in range(0,n_eqc):        
                for k in range(0,pickedSolution[j]):
                    print("edge between ",DS[hub][0]," and ",eqc[j][k])
                    Gr.add_edge(DS[hub][0],eqc[j][k])
                    for l in range(0,len(DS)):
                        if DS[l][0]==eqc[j][k]:
                            DS[l][1]-=1
                            DS[hub][1]-=1
                            resetConnections.append(eqc[j][k])
            DS3=[]
            DS3=DS        
            reccReturn=recc(DS3,hub+1)
            DS[hub][1]+=len(resetConnections)
            #we do a reset to make sure the different solutions are explored independently 
            for j in resetConnections:
                for k in range(0,len(DS)):
                    if j==DS[k][0]:
                        Gr.remove_edge(DS[hub][0], j)
                        DS[k][1]+=1

class JRGraph:
    def __init__(self,N,DS):
        self.n=N
        self.DegreeList=DS
        #sort through the degrees and arrange them in decreasing order
        self.DegreeList.sort(reverse=True)
        self.NodeList= []
        for i in range(1,self.n+1):
            self.NodeList.append(i)
        #make a dictionary list with the keys being the nodes and the values being the degrees
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
        reccReturn=recc(DS,-1)
        
  
            
            
        




