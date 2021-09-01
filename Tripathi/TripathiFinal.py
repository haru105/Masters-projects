#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:29:59 2021

Notes for the user:

This program takes input from the user for n: the number of nodes and Seq: degree sequence.
A graph is then built for this degree sequence using the method prescribed by Tripathi 
in [1]
The construction is done through the construction of sub-realizations of the graph 
using five different cases
Let 
    the node to be saturated be r (r going from 0 to n-1), 
    set of nodes to the left of r be F,
    set of nodes to the right of r be S
case 0: straightforward saturation where there are nodes left in S to join to r
case 1: No more nodes in S to connect r to
   1.1: when r's desc is 2, find edge i-u (i from F and u which is a neighbor of i);
      - replace with r-u and r-i
   1.2: when r's desc is 1, find edge r-k and u-i (i from F, k from S, 
        and u which is a neighbor of i);
      - replace with r-u and r-i
case 2: No nodes in F that meet the requirements in case 1
        Find edges r-k and i-u (i from F, k from S,u which is a neighbor of i); 
      - replace u-i with r-u and k-i
case 3: No nodes that meet the requirement from case 1 and 2
        Find edges w-j and i-u (i and j from F, w and u from S); 
      - replace them with i-j and r-u
case 4: erdos gallai test 
As soon as r gets fully saturated, it gets incremented

References:n 
[1] Tripathi, A., Venugopalan, S., & West, D. B. (2010). A short constructive
proof of the Erdős–Gallai characterization of graphic lists. Discrete mathematics, 
310(4), 843-844.

"""


import networkx as nx 
import matplotlib.pyplot as plt 
import copy
import TripathiFunctionsFinal as tpt

class EGtree:

     def __init__(self, noNodes, seq):
         self.noNodes = noNodes #number of nodes
         self.DSeq = seq #List of prescribed degree of sequence
         self.DSeq.sort(reverse=True) #Making the degree sequence non-increasing
         self.GenTreeWithCases(self.noNodes, self.DSeq)
         
     def GenTreeWithCases(self, nq, DSeq):
    #This function analyses the degree sequence and splits in such a 
    #way that makes the generation fall through 5 different cases
        G = nx.empty_graph(nq)
        h=1
        #tpt.displayGraph(G) #Initiating the process with a graph with empty nodes
        Seq=copy.deepcopy(DSeq) #Preserving the target degree sequence
        print ("\nStarting case based Tree generation for",Seq,"\n")
        # Outer loop
        r=0
        while r<nq:
            
            #br controls the loop and acts as a flag value that stands for whether a node is saturated or not 
            #Initially every node is unsaturated and has the br value as 0
            #As every case is iterated through, the br value gets pdated to 1 iff it is saturated
            # when the br value is 1, the iterator breaks out of the inner loop and moves on the next node
            #and tpt.test_case_4(r,DSeq,Seq)==True
            if Seq==[0]*nq:
                print( "DONE")
                nx.draw(G, with_labels=True, node_color="white",edgecolors='black', font_weight='bold')
                plt.title('Tripathi graph')
                plt.show()
                return()
            print("\nsaturating ", r)
            if Seq[r]==0:
                r+=1
            
        	# Inner loop
            while Seq[r]!=0:
                # self.graphs[h]=G
                # h+=1
                if Seq==[0]*nq:
                    print ("DONE")
                    plt.show()
                    return()               
                F=[] 
                #this list maintains the indices lesser than r, also referred to as vi in the paper
                F=range(0,r)
                F=list(F)

                if r==nq-1:
                    S=[]
                else:
                    S=range(r+1,nq) #refers to the independent set S that goes from indices more than r
                    S=list(S)

                Seq,G=tpt.test_case_0(r,Seq,G,S)

                if(Seq[r]==0):
                    r+=1
                    print ("r updated to ",r)
                    break

                Seq,G=tpt.test_case_1(nq,r,Seq,G,S,F)

                if(Seq[r]==0):
                    r+=1
                    print ("r updated to ",r)
                    break

                Seq,G=tpt.test_case_2(r,Seq,G,S,F)

                if(Seq[r]==0):
                    r+=1
                    print ("r updated to ",r)
                    break

                Seq,G=tpt.test_case_3(r,Seq,G,S,F)

                if(Seq[r]==0):
                    r+=1
                    print ("r updated to ",r)
                    break  
                print("trial")
                return()

        if r==nq and Seq==[0]*nq:
            print("DONE")
            nx.draw(G, with_labels=True, node_color="white",edgecolors='black', font_weight='bold')
            plt.show()
            return()
        
 
def pp(n,L):
    gd= EGtree(n,L,1)
    
def main():
    nq = int(input("Enter no. of nodes:"))
    lst=[]
    print("\n Enter the degrees of the nodes one by one \n")
    for i in range(0, nq):
        ele = int(input()) 
        lst.append(ele) #adding the element to the degree list
    if(tpt.graphic(lst)): #to verify is degree sequence is realizable using erdos gallai's theorem
         print ("Graph is realizable")
         gd = EGtree(nq,lst)
    else:
        print ("Graph is not realizable")

if __name__ == "__main__":
    main()

