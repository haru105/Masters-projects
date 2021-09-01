#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:55:44 2021

@author: amreethrajan
"""

 
import sys
import networkx as nx
import matplotlib.pyplot as plt
import random
import networkx.algorithms.graphical as funs 
import copy 
import binarySearch as bs

class KimG:
    def __init__(self,n,degrees):
        self.number_of_nodes=n
        self.DegList=degrees
        self.DegList.sort(reverse=True)
        self.NodeList=[]
        self.G=nx.Graph()
        
        for i in range(1,n+1):
            self.NodeList.append(i)
            
        self.G.add_nodes_from(self.NodeList)
        self.DS=[]
        #DS is a double list with nodes and degrees
        for i in range(0,self.number_of_nodes):
            self.DS.append([self.NodeList[i],self.DegList[i]])
            
        if funs.is_valid_degree_sequence_erdos_gallai(self.DegList)==True:
            self.SampGen()
            nx.draw(self.G,with_labels=True, node_color="white",edgecolors='black', font_weight='bold')
            plt.title("Kim's sampling Graph")
            plt.show()
        else:
            print("The inputted sequence is not graphical and cannot be processed")
        
    
    def SampGen(self):
        self.DS1=copy.copy(self.DS)
        saturation=0
        hub=0
        chosen_node=0
        
        #the loop goes on until saturation
        while saturation==False:
            allowed_nodes=[]
            forbidden_nodes=[]
            
            #First node is assigned as hub node, and is added to the forbidden list
            forbidden_nodes.append(self.DS[0][0])
            hub=self.DS[0][0]
            
            print("\n\nHub node: ",hub)
            print("Degree sequence before making any connections: ",self.DS)
            print("Connection #1 i.e. the straightforward one:")
            
            #The first connection to the hub node never causes failure
            #So, we pick a random node and make connections
            
            #Everything other than the first node is added to the allowed list
            allowed_nodes=[x[0] for x in self.DS[1:]]
            
            #Node is randomly picked from the allowed list
            chosen_node=random.choice(allowed_nodes)
            print(chosen_node," is the chosen node from the list ",allowed_nodes)
            
            #Locate the randomly chosen node in the double list DS
            #and reduce the degrees of the hub node and the chosen node
            for i in self.DS:
                if i[0]==chosen_node:
                    i[1]-=1
                    self.DS[0][1]-=1
                    break
                
            #Introduce edge between hub node and chosen node
            self.G.add_edge(hub,int(chosen_node))
            
            #Add chosen node to the forbidden nodes as well
            forbidden_nodes.append(chosen_node)
            print("Connection successful")
            print("Forbidden nodes: ",forbidden_nodes)
            
            
            hub_degree=self.DS[0][1]
            #This loop goes on until the hub node is saturated
            while hub_degree!=0:
                print("-----------------------------")
                print("The degree to be satisfied: ",hub_degree)
                
                #reset allowed nodes
                allowed_nodes=[]
                non_forbidden_nodes=[]
                
                #first collect nodes that are not in the forbidden list
                for i in self.DS:
                    if (i[0] not in forbidden_nodes) and (i[1]!=0):
                        non_forbidden_nodes.append(i)
                        
                print("Nodes that might be eligible for connection ",[x[0] for x in non_forbidden_nodes])
                non_forbidden_nodes.sort(key=lambda x:x[1], reverse=True)
                leftmost_set=[] 
                DS2=copy.deepcopy(self.DS)
                
                if hub_degree!=1:
                    
                    #build leftmost set [if degree of the hub node is three, 
                    #then in a non increasing list, the first three nodes 
                    #form the leftmost set. leftmost nodes don't cause failure
                    #, so they need to be removed to locate where the failure 
                    # happens]
                    for i in range(0,hub_degree):
                        leftmost_set.append(non_forbidden_nodes.pop(0))
                        
                    #we connect the hub node to all but one nodes from the leftmost 
                    #set so that the hub node's degree is 1
                    for i in self.DS:
                        if i in leftmost_set[0:(len(leftmost_set)-1)]:
                            self.DS[0][1]-=1
                            i[1]-=1
                else:
                    #if the hub degree is already one, we don't need to make 
                    #temporary connections
                    leftmost_set.append(non_forbidden_nodes.pop(0))
                print("Leftmost adjacent set: ",leftmost_set)
                print("Temporarily joining hub node to reduce it's degree to 1")
                print("Temporarily changed degree sequence: ",self.DS)                
                #the bigger degree sequence        

                if non_forbidden_nodes!=[]:
                    for i in range(0,len(self.DS)):
                        if self.DS[i][0]==hub:
                            self.DS[i][1]-=1
                    #we reduce the hub node's degree to 0 before checking for
                    #failure nodes. 
                    valid_nodes=bs.binarySearch(non_forbidden_nodes,self.DS)
                    #the binary search function returns the non forbidden list
                    #with all the failure nodes returned

                else:
                    #sometimes there are no valid non-forbidden nodes
                    valid_nodes=[]
                    
                print("Leftmost set is ",leftmost_set)
                leftmost_nodes=[x[0] for x in leftmost_set]
                
                #ultimately the leftmost nodes and the other valid nodes are 
                #combined to make up the allowed list
                print("appending ",leftmost_nodes," and ",valid_nodes)
                for i in leftmost_nodes:
                    allowed_nodes.append(i)
                if valid_nodes!=[]:
                    for i in valid_nodes:
                        allowed_nodes.append(i)
                print("Allowed nodes after removing failure nodes: ",allowed_nodes)
                
                #Restoring degree sequence to before temporary test connections
                self.DS=copy.deepcopy(DS2)
                
                #Once the allowed set is built, a node is picked at random
                chosen_node=random.choice(allowed_nodes)
                print("Chosen node : ",chosen_node)
                
                #Make connection and update degree sequence
                for i in self.DS:
                    if i[0]==chosen_node:
                        i[1]-=1
                        self.DS[0][1]-=1
                        break
                self.G.add_edge(hub,int(chosen_node))
                print("Connection successful")
                
                #After every connection for a hub node, we add the node to the
                #forbidden list
                forbidden_nodes.append(chosen_node)
                
                hub_degree=self.DS[0][1]
                
            print("-----------------------------")
            print(hub," has been fully saturated") 
            DS3=copy.copy(self.DS)
            
            #Remove nodes that have been saturated
            for i in range(0,len(DS3)):
                if DS3[i][1]==0:
                    self.DS.remove(DS3[i])
            self.DS.sort(key= lambda x:x[1],reverse=True)
            print("Newly sorted list: ",self.DS)
            self.DegList=[x[1] for x in self.DS]
            
            #Check if all nodes are saturated
            if self.DegList==len(self.DegList)*[0] or self.DegList==[]:
                saturation=True
                print("All nodes have been saturated\nGraph generation done! ")