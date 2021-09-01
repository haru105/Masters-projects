#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 04:04:18 2021

@author: amreethrajan

"""
import networkx as nx
import matplotlib.pyplot as plt
import random
import networkx.algorithms.graphical as funs 
import copy 

#This function does a random selection of a smaller set given the rightmost
# adjacency list for the node options available
def SmallSet(nodes,rightmost):
    print("Nodes allowed: ",nodes," Rightmost: ",rightmost)
    smallset=[]
    LowerLimit=min(nodes)
    for i in range(0,len(rightmost)):
        randPick=-1
        while randPick not in nodes:
            randPick=random.randint(LowerLimit,rightmost[i])
        smallset.append(randPick)
        #LowerLimit gets updated 
        LowerLimit=randPick+1
    print("Picked indices of nodes to saturate:  ",smallset)
    return smallset

Gr=nx.Graph()

#this variable guides the recursion
# recur=1

#the recursive function that recursively processes the nodes until the needed graph is produced
def recGen(DS):
    global recur
    global Gr
    DS.sort(key=lambda x:x[1], reverse=True)
    print("Recursing for sequence: ",DS)
    
    #DS is a 2D that maintains node labels and degrees
    #we collect the node labels and degrees into two lists
    NodeList=[x[0] for x in DS]
    DegreeList=[x[1] for x in DS]
    n=len(NodeList)

    #the generation would not even take place if the degree sequence isn't graphical
    if funs.is_valid_degree_sequence_erdos_gallai(DegreeList)==False:
        return 0
   
    #when we have a graphical sequence and when we no longer have nodes to process we end the process
    elif DegreeList==len(DegreeList)*[0] or DS==[]:
        print("Graph done")
        print("Graph completed")
        nx.draw(Gr,with_labels=True, node_color="white",edgecolors='black', font_weight='bold')
        plt.title('Kims Graph')
        plt.show()
        return 1
        # sys.exit() 
        
    #when the node being processed is already fully saturated
    elif DegreeList[0]==0:
        print("Skipping this node since it's already saturated")
        DS2=DS
        DS2.pop(0)
        RecReturn=recGen(DS2)
        if RecReturn==1:
            return 1
        return 
   
    else:
        RightMarker=n-1
        #RightMarker is set in a way that makes us process the nodes right to left
        
        DS3=copy.deepcopy(DS)
        #we need to create a copy of the original sequence since we need to 
        #make some experimental changes to determine the viability of the action
        
        #this stores the rightmost adjacency list
        RightmostAdjSet=[]
        
        #this stands for the selected option to proceed
        PickedNodeSet=[]
        while (RightMarker>0):
            # if DegreeList!=len(DegreeList)*[0] and DS3!=[]:
            DS3[0][1]-=1
            DS3[RightMarker][1]-=1
            #we first make the connection and then determine its viability
            NodeList=[x[0] for x in DS3]
            DegreeList=[x[1] for x in DS3]

            print("Checking if connection is viable between ",NodeList[0]," and ",NodeList[RightMarker])
            if(funs.is_valid_degree_sequence_erdos_gallai(DegreeList) and Gr.has_edge(NodeList[0],NodeList[RightMarker])==False):
                print("Connection viable")
                Gr.add_edge(NodeList[0],NodeList[RightMarker])
                RightmostAdjSet.append(RightMarker)
                
            else:
                print("Connection not viable")
                DS3[0][1]+=1
                DS3[RightMarker][1]+=1
                
            if DS3[0][1]!=0:
                RightMarker-=1
            else:
                print("Node processing completed \n \n")
                RightMarker=0
            NodeList=[x[0] for x in DS3]
            DegreeList=[x[1] for x in DS3]
        
        #we leave the while loop with a rightmost adjacenct list on hand
        NodeList=[x[0] for x in DS3]
        DegreeList=[x[1] for x in DS3]
        
        #this list needs to be sorted for computation purposes
        RightmostAdjSet.sort()
        
        for i in RightmostAdjSet:
            Gr.remove_edge(NodeList[0],NodeList[i])
            #we undo all the experimental edge creations
            
        NodeList3=[x[0] for x in DS3]
        HubLessNodeList=list(range(1,len(DS3)))
        
        #the if-else here is to differentiate between the scenarios of either 
        #having to make smaller sets i.e. when the degree sequence is nto exhausted
        # vs the scenario of not needing to pick smaller sets since the degree sequence 
        #is all exhausted
        
        if DegreeList!=len(DegreeList)*[0]:
            print("Picking a smaller set for the rightmost adjacency set at indices: ",RightmostAdjSet)
            smallset=SmallSet(HubLessNodeList,RightmostAdjSet)
            PickedNodeSet=[]
            #PickedNodeSet=SmallSet(HubLessNodeList,RightmostAdjSet)
            for i in smallset:
                PickedNodeSet.append(NodeList3[i])
            print("Picked set of nodes: ",PickedNodeSet)
            for i in PickedNodeSet:
                print("Edge created between ",NodeList[0]," and ",i)
                Gr.add_edge(NodeList[0],i)
                DS[0][1]-=1
                for j in DS:
                    if j[0]==i:
                        j[1]-=1

            DS4=copy.deepcopy(DS)
            for i in DS4:
                if i[1]==0:
                    DS.remove(i)       
            DS4=copy.deepcopy(DS)
            #Once we reinforce our choice, we recursively do the same for
            #the rest of the smalller sets
            RecReturn=recGen(DS4)
            if RecReturn==1: #to end the recursion since all nodes are saturated
                return 1
        else:
            for i in RightmostAdjSet:
                print("Edge created between ",NodeList[0]," and ",NodeList3[i])
                Gr.add_edge(NodeList[0],NodeList3[i])
                DS[0][1]-=1
                for j in DS:
                    if j[0]==NodeList3[i]:
                        j[1]-=1
            #print("2: DS before removing zero entries: ",DS)
            DS4=copy.deepcopy(DS)
            for i in DS4:
                if i[1]==0:
                    DS.remove(i)
            DS4=copy.deepcopy(DS)
            RecReturn=recGen(DS4)
            if RecReturn==1:
                return 1
        return
    
    
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
        self.rootGen()
        
    
    def rootGen(self):
        global Gr
        global recur
        DS=self.DS
        NodeList=[x[0] for x in DS]
        DegreeList=[x[1] for x in DS]
        #we determine at the start wheter the sequence is graphical or not
        
        #when the sequence is not graphical we exit the code after indicating that
        if funs.is_valid_degree_sequence_erdos_gallai(DegreeList)==False:
            print("Degree sequence entered is invalid")
            return

        #we start the construction process when we know that the sequence is graphical
        else:
            Gr.add_nodes_from(NodeList)
            r=recGen(DS)
            
        
    