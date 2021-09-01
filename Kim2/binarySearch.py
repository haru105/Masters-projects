#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 22:46:42 2021

@author: amreethrajan
"""

import networkx.algorithms.graphical as funs 
import copy
import math

def binarySearch(non_forbidden_nodes1,DS):
    #'DS' is the full degree sequence with the nodes with their degrees
    
    #'non_forbidden_nodes' are the nodes that are eligible for connection 
    # but need to be checked for causing graphicality test failure
    
    # Our goal is to find the node label at which the erdos test fails
    # and return the valid nodes for connection to hub node
    
    non_forbidden_nodes=copy.copy(non_forbidden_nodes1)
    DS1=copy.copy(DS)

    end=len(non_forbidden_nodes)-1
    start=0
    mid=math.floor((start+end)/2)

    print("Start: ",start," Mid: ",mid," End: ",end,"\n")
    
    while (end-start)>=0:
        mid=math.floor((start+end)/2)
        print("Start: ",start," Mid: ",mid," End: ",end,"\n")
        
        #we first locate the middle node reduce it's degree  temporarily 
        for i in range(0,len(DS1)):
            if non_forbidden_nodes[mid][0]==DS1[i][0]:
                DS1[i][1]-=1
        
        #we then extract the degrees alone to check the sequence's realizability
        DegList=[x[1] for x in DS1]
        DegList.sort(reverse=True)
        print("The sorted sequence that's gonna be checked is: ",DegList)
        
        realizability=funs.is_valid_degree_sequence_erdos_gallai(DegList)
        
        if realizability==True:
            print("This is a successful degree sequence")
            start=mid+1
            flag=1
        else:
            print(non_forbidden_nodes[mid][0]," is a failure node")
            end=mid
            flag=0

        #we revert back the middle node's degree 
        for i in range(0,len(DS1)):
            if non_forbidden_nodes[mid][0]==DS1[i][0]:
                DS1[i][1]+=1 
                
        if start==end==mid:
            break
     
    #'flag' is false when failure node exists   
    
    #valid_nodes will hold all the nodes that don't fail the realizability
    valid_nodes=[]
    
    if flag==True:
        for i in range(0,len(non_forbidden_nodes1)):
            valid_nodes.append(non_forbidden_nodes1[i][0])
    else:
        for i in range(0,start):
            valid_nodes.append(non_forbidden_nodes1[i][0])
            
    return valid_nodes
        

            
            
            