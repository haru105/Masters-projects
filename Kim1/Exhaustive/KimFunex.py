#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 04:04:18 2021
@author: amreethrajan

A few notes: 
    The repeated action is as follows:
    For every hub node calculated, a rightmost adjacent set is calculated. The
    rightmost adjacent set defines a boundary within which no failures occur.
    Every adjacent set that is lexicographically smaller than this set never 
    break graphicality. 
    
    The repeated actions are carried out recursively to generate all the graphs 
    (from a limited space) that realize the inputted degree sequence. At every 
    step a hub node is picked, and a rightmost adjacent step is calculated. 
    This is followed by the calculation of the set of smaller sets. We iterate 
    through each of the smaller set. For each smaller set, nodes are connected 
    accordingly and update the sequence and recurse again for the updated 
    degree sequence. When a passed degree sequence indicates that all the nodes 
    have been saturated, we display a graph and return back a step to process
    a different smaller set. 
    
    Finally when all the smaller steps at all levels have been explored, we 
    return to the main and end the process. 
    
"""
import copy
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.graphical as funs 
import itertools

Gr=nx.Graph()

def BuildSet(nodes,rightmost):
    #builds the smaller sets wrt rightmost adjacent list
    Range_of_smallersets=range(min(nodes),rightmost[len(rightmost)-1]+1)
    SmallerSets=list(itertools.combinations(Range_of_smallersets,len(rightmost)))
    #The SmallerSets initially has all the combinations
    print("rough smaller sets: ",SmallerSets)
    #We now need to remove some of the incorrect sets that are bigger
    #that the rightmost
    removal_sets=[]
    for i in range(0,len(SmallerSets)):
         for j in range(0,len(rightmost)):
             if SmallerSets[i][j]>rightmost[j]:
                 removal_sets.append(SmallerSets[i])
                 break
                 # SmallerSets.remove(i)
    print("Sets to be removed", removal_sets)
    for i in removal_sets:
        SmallerSets.remove(i)
    return SmallerSets

CountGraphs=0

def recGen(DS):
    global Gr
    global CountGraphs
    DS1=copy.copy(DS)
    #Preserving degree sequences since different paths have to be explored
    
    #Removing fully saturated nodes
    for i in DS1:
        if i[1]==0:
            DS.remove(i)
    
    DS.sort(key=lambda x:x[1],reverse=True)

    #unzipping double list into nodes and degrees
    DegreeList=[x[1] for x in DS]
    NodeList=[x[0] for x in DS]
    
    n=len(DegreeList)
    
    #success path
    if DegreeList==n*[0]:
        print("\nSuccessful path!\n\n")
        CountGraphs+=1   
        return 1
    
    else:
        rightMarker=n-1
        #to construct the rightmost adjacent list
        #we start from the last element and keep 
        #decrementing it as we go 
        
        RightmostAdjSet=[]
        #this list is to maintain all the nodes 
        #that pass the CG test 
        
        DS4=list(DS) #temporary list to find rightmost adjacency set
        while (rightMarker>0):
            # if DegreeList!=len(DegreeList)*[0] and DS4!=[]:
            DS4[0][1]-=1
            DS4[rightMarker][1]-=1
            #we first make the connection and then determine its viability
            NodeList=[x[0] for x in DS4]
            DegreeList=[x[1] for x in DS4]
            if(funs.is_valid_degree_sequence_erdos_gallai(DegreeList) and Gr.has_edge(NodeList[0],NodeList[rightMarker])==False):
                Gr.add_edge(NodeList[0],NodeList[rightMarker])
                RightmostAdjSet.append(rightMarker)
            else:
                DS4[0][1]+=1
                DS4[rightMarker][1]+=1
            if DS4[0][1]!=0:
                rightMarker-=1
            else:
                rightMarker=0
            NodeList=[x[0] for x in DS4]
            DegreeList=[x[1] for x in DS4]
            
        if DegreeList==[0]*len(DegreeList): #when successful graph can be outputted
            nx.draw(Gr,with_labels=True, font_weight='bold')
            plt.title('Kim Graph')
            plt.show()
            
        RightmostAdjSet.sort()
        #Once we're out of the while loop, we're 
        #done with rightmost adjacent list
        
        for i in RightmostAdjSet:
            Gr.remove_edge(NodeList[0],NodeList[i]) 
            #removing the temporary edges made to calculate rightmost adjacency set
            
        SolutionList=[]
        MappedNodeLabels=[]
        print("DS is",DS) 
        DS5=copy.copy(DS)
        
        if DegreeList!=len(DegreeList)*[0]:
            print("The rightmost adjacent list is ",RightmostAdjSet)
            
            #Find the smaller sets
            O=BuildSet(range(1,len(DS4)),RightmostAdjSet)
            #O contains the indices of the nodes 
            print("The sets built: ",O)

            #we now need to map the indices to the node labels 
            for i in range(0,len(O)):
                for j in range(0,len(O[i])):
                    MappedNodeLabels.append(NodeList[O[i][j]])                  
            SolutionList=[MappedNodeLabels[w:w+len(RightmostAdjSet)] for w in range(0, len(MappedNodeLabels), len(RightmostAdjSet))]
           
            for i in RightmostAdjSet:
                for j in DS5:
                    if NodeList[i]==j[0]:
                        j[1]+=1 #undo-ing the temporary changes to DS 
                        
            DS5[0][1]=len(RightmostAdjSet) 
            
            for ChosenSolution in SolutionList:
                DS5=DS
                print("Process solution: ",ChosenSolution)
                
                for i in ChosenSolution:
                    Gr.add_edge(NodeList[0],i)
                    print("introducing edge between ",NodeList[0]," and ",i)
                    for j in DS5:
                        if i==j[0]:
                            j[1]-=1
                            DS5[0][1]-=1
                            break
                        
                DS6=[]
                DS6=copy.copy(DS5)
                recReturn=recGen(DS6)
                
                #Undo the edges and degree sequence updates to explore 
                #a different smaller step at the same level
                for i in ChosenSolution:
                    Gr.remove_edge(NodeList[0],i)
                    for j in DS5:
                        if i==j[0]:
                            j[1]+=1
                            DS5[0][1]+=1
                            break        
        else:
            #Undo degree sequence updates to go back up a step to explore a 
            #different smaller step on a previous level
            recReturn=recGen(DS5)
            for i in RightmostAdjSet:
                for j in DS:
                    if NodeList[i]==j[0]:
                        j[1]+=1
            DS[0][1]=len(RightmostAdjSet)
            
class KimG:
    def __init__(self,N,DS):
        self.n=N
        self.DegreeList=DS
        self.DegreeList.sort(reverse=True)
        self.NodeList=[]
        for i in range(1,N+1):
            self.NodeList.append(i)
        self.DS=[]
        for i in range(0,self.n):
            self.DS.append([self.NodeList[i],self.DegreeList[i]])
        print(self.DS)
        self.rootGen()
    
    def rootGen(self):
        global Gr
        global RecControl
        global CountGraphs
        DS=self.DS
        NodeList=[x[0] for x in DS]
        Gr.add_nodes_from(NodeList)
        recReturn=recGen(DS)
        print("Count is : ",CountGraphs)