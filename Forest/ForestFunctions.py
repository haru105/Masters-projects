#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:19:08 2020
The functions for forest generation, with more changes to ensure correectness 
Version :2
@author: amreethrajan
"""
import networkx as nx 
import matplotlib.pyplot as plt 

def displayForest(F):
    # A function to display the forest that's generated in previous functions
    print ("Displaying forest")
    plt.figure()
    nx.draw(F, with_labels=True, font_weight='bold')
    plt.title('Forest generation')
    plt.show()
        
def ForestCompCheck(F,Seq):
    # Do a check to see if the nodes are saturated or not 
    # If the forest is done being gnenerated, then 1 is returnedd
    if Seq==[0]*(len(Seq)-1):
        return 1    
    else:
        return 0
   
def ForCheck(n,Seq):
    # The function checks for the condition where the sum of the degrees should 
    # be lesser than or equal to 2(n-1). 
    
    fsum= 0
    for i in Seq:
        #Calculate degree sum
        fsum+= i
    
    #First make sure that the degree sum is even
    #Then check if the forest condition established, is satisfied 
    if(fsum%2==0 and fsum<=(2*n-1)):
        return 1
    else:
        return 0

def ForestGen(m,DSeq,F):

    vis=m*[0] 
    # vis denotes a list denoting the status of a node in terms of 
    # whether the node has been visited or not 

    DSeq.sort(reverse=True)
    #print Dseq
    i=0
    
    while(DSeq!=m*[0]):
        #If all the nodes are not saturated 
        print("processing node: ",i)
        
        for j in range(i+1,m):
            # check if the nodes involved in the edge formation are not saturated
            # Also make sure that already visited nodes are not joined to the node
            if(DSeq[i]!=0 and DSeq[j]!=0 and vis[j]==0): 
                
                F.add_edge(i,j)
                print("adding edge between ",i," and ",j)
                DSeq[i]-=1
                DSeq[j]-=1
                #Update the degree sequence after edge formation
                
                vis[j]=1
                #Mark the node as visited so that cycles don't get formed
                displayForest(F)
                
        #Finding the next unsaturated node to saturate
        for n in range(i+1,m):
            if DSeq[n]!=0:
                break
        i=n
        
    return F
        
