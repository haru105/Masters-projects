#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 01:06:05 2021

@author: amreethrajan
"""
import networkx as nx
import matplotlib.pyplot as plt
import random
    
class SplitG:
    def __init__(self,n,DS):
        self.N=n
        self.Dlist=DS
        self.Dlist.sort(reverse=True)
        self.Nlist=[]
        #initializing the nodes from 1 to n
        for i in range(1,n+1):
            self.Nlist.append(i)
        self.L=[]
        #initializing a double list to maintain index-degree integrity
        for i in range(0,self.N):
            self.L.append([self.Nlist[i],self.Dlist[i]])
        #checking if degree sequence meets the split graph conditions
        stat,m=self.splitcon(self.L,self.N)
        #function returns whether DS is split graphical and 
        #highest value of i for which di≤i-1
        if(stat):
            self.Gr=nx.Graph()
            self.Gr.add_nodes_from(self.Nlist)
            self.splitgen(m,self.L,self.N)
            nx.draw(self.Gr,with_labels=True, node_color="white",edgecolors='black', font_weight='bold')
            plt.title('Split Graph')
            plt.show()

        else:
            print("Degree sequence does not satisfy split graph conditions")
        
    def splitgen(self,m,L,N):
        #first make the induced connected graph 
        for i in range(0,m-1):
            for j in range(i+1,m):
                self.Gr.add_edge(self.Nlist[i],self.Nlist[j])
                print("Edge between ",self.Nlist[i]," and ",self.Nlist[j])
                self.Dlist[i]-=1
                self.Dlist[j]-=1
                
        
        #here we connect the independent set to the induced connected graph 
        for i in range(m,N):
            cand=[]
            #candidate list is computed 
            #candidate list contains nodes with non zero degrees that haven't 
            # been connected to the hub node yet
            for j in range(0,m):
                    if self.Dlist[j]!=0 and  self.Gr.has_edge(self.Nlist[i],self.Nlist[j])==False and i!=j:
                        cand.append(L[j])
                        
            #until hub node is not saturated
            while self.Dlist[i]!=0:   
                p=random.randint(0,(len(cand)-1))
                self.Gr.add_edge(self.Nlist[i],cand[p][0])
                print("Edge between ",self.Nlist[i]," and ",cand[p][0])
                self.Dlist[i]-=1
                for u in range(0,len(L)):
                    if cand[p][0]==L[u][0]:
                        break
                self.Dlist[u]-=1
                del cand[p]                
                    
        
    def splitcon(self,L,N):
        m=0
        
        for i in L:
            if i[1]>=(i[0]-1):
                m=i[0]
            else:
                break
        #find split poiny    
        print("m is : ",m)
        lhs=0
        rhs=0
        
        #check the split graph conditions 
        for i in range(0,m):
            lhs+=L[i][1]
        rhs+=m*(m-1)
        for i in range(m,N):
            rhs+=L[i][1]
            
        if lhs==rhs and m!=N:
            return True,m
        else:
            return False,m
        
        
        
