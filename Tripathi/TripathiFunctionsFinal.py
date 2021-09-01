#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 10:28:49 2021

@author: amreethrajan
User notes:
This file contains the code for the different cases mentioned 
in the main file

"""
import networkx as nx 
import random
g=1

def graphic(seq):
    sum1=0
    sum2=0
    sum3=0
    for i in seq:
        sum3+=i
    r=random.randint(1,(len(seq)))
    for i in range(0,r):
        sum1+=seq[i]
    sum2+=(r*(r-1))
    for i in range(r,len(seq)):
        sum2+=min(r,seq[i])
    # print("r: ",r,"; sum1: ",sum1," ;sum2: ",sum2)
    if sum1<=sum2 and sum3%2==0:
        return True
    else:
        return False

#this function deals with the case 0 condition checking and edge addition 
def test_case_0(r,Seq,G,S):
    res=list(S)
    random.shuffle(res) #the concept of picking a random node is implemented by shuffling the list 
    for i in res:
        if (Seq[i]!=0) and (Seq[r]!=0) and (G.has_edge(r,i)==False): #check if the picked node is saturated and if there is an edge between it and r
            print ("\nCASE 0 ENTERED")
            #Add the edges 
            print("\t adding edge ",r,"and ",i) 
            G.add_edge(r, i)
            #updating degree descrepancies
            Seq[r]-=1
            Seq[i]-=1
            print ("Degree sequence:")
            print (nx.degree(G))
    return Seq,G

def test_case_1(nq,r,Seq,G,S,F):
    for i in F: #Checking if there are any nodes left that isn't connected to r
        if G.has_edge(i,r)==False: #this means there are nodes left
            break
    if Seq[r]>=2: #checking if the deficiency of r is greater than or equal to 2
            for u in list(G.neighbors(i)):
                if u not in list(G.neighbors(r)):
                # if(G.has_edge(i,u)== True and G.has_edge(u,r)==False) and (u not in G.neighbors(r)):
                    print ("\nCase 1: Descrepancy 2")
                    #replacing edge pb with pr and br
                    G.remove_edge(u,i)
                    G.add_edge(i,r)
                    G.add_edge(u,r)
                    print("\t removing edge ",i,"and ",u) 
                    print("\t adding edge ",r,"and ",i) 
                    print("\t adding edge ",r,"and ",u) 
                    #updating degree descrepancies
                    Seq[r]-=2
                    print ("Initial graph for degree:")
                    print (nx.degree(G))
                    #displayGraph(G,r)
                    return Seq,G

    elif Seq[r] == 1: #checking if deficiency of r is 1
        for u in list(G.neighbors(i)):
            if u not in list(G.neighbors(r)):
                for k in list(G.neighbors(r)):
                    if u!=k and k>r:
                        print ("\nCase 1: Descrepancy 1")
                        #replacing edge ab and cr with ar and bc
                        G.remove_edge(i,u)
                        G.remove_edge(k,r)
                        G.add_edge(i,r)
                        G.add_edge(u,r)
                        print("\t removing edge ",i,"and ",u) 
                        print("\t removing edge ",k,"and ",r)
                        print("\t adding edge ",r,"and ",i) 
                        print("\t adding edge ",r,"and ",u)
                        #updating degree descrepancies
                        Seq[r]-=1
                        Seq[k]+=1
                        print ("Initial graph for degree:")
                        print (nx.degree(G))
                        #displayGraph(G,r)
                        return Seq,G
    return Seq,G

def test_case_2(r, Seq,G,S,F):
    print("\a")
    for i in F: #when there are no nodes with index lesser than i that's unsaturated
        for k in S:
            if(G.has_edge(i,k)==False and G.has_edge(k,r)==True and Seq[k]<=r and Seq[k]!=0):
                for u in list(G.neighbors(i)):
                    if u not in list(G.neighbors(r)):
                    # if(G.has_edge(u,i)==True and G.has_edge(u,r)==False):
                        print ("\nCASE 2 ENTERED")
                        #relacing edge ui with ur and ik
                        print("\a\a")
                        G.remove_edge(u,i)
                        G.add_edge(u,r)
                        G.add_edge(i,k)
                        print("\t removing edge ",u,"and ",i) 
                        print("\t adding edge ",r,"and ",u) 
                        print("\t adding edge ",i,"and ",k)
                        #updating degree descrepancies
                        Seq[r]-=1
                        Seq[k]-=1
                        print ("Initial graph for degree:")
                        print (nx.degree(G))
                        return Seq,G             
    return Seq,G

def test_case_3(r,Seq,G,S,F):
    print("\a")         
    for i in F:
        for j in F[i+1:]:
            if(G.has_edge(i,j)==False):
                for u in list(G.neighbors(i)):
                    if u not in list(G.neighbors(r)):
                        for w in list(G.neighbors(j)):
                            if w not in list(G.neighbors(r)):
                                print("\a\a\a")
                                print ("\nCASE 3 ENTERED")
                                G.remove_edge(i,u)
                                G.remove_edge(j,w)
                                G.add_edge(i,j)
                                G.add_edge(u,r)
                                print("\t removing edge ",i,"and ",u) 
                                print("\t removing edge ",j,"and ",w)
                                print("\t adding edge ",i,"and ",j) 
                                print("\t adding edge ",r,"and ",u)
                                #updating degree descrepancies
                                Seq[r]-=1
                                Seq[w]+=1
                                return Seq,G
    return Seq,G
        

