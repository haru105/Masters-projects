# Masters-projects
Collection of the projects i've worked on in my time pursuing a masters degree in Computer Science. My thesis was majorly focused on generating graphs from degree sequences
A graph can be considered to be a collection of vertices/nodes and edges. The graphs that are going to be generated here specifically are labelled graphs with no multiple edges nor self loops. 
* Graph generation can be understood as the process of constructing graphs of a given class. 
* Graph generation can be used to create catalogues of graphs for making conjectures about classes of graphs, by generating examples of the class of graphs and observing them. Example: For the conjecture all regular graphs have Hamiltonian cycles, would call for generating examples of regular graphs and observing them. 
* Conjectures can also be refuted in a similar manner. Another example application of graph generation is to provide test instances for algorithms for a given class of graphs. Example: An algorithm  that tests if a graphs is strongly chordal, we would need to generate the graph that is going to be tested. 

Hakimi's generation and Tripathi's generation focuses on some preliminary and foundation methods that can help establish the basics of graph generation
Forests and Split graphs are special cases that extend the basic graph generation principles to cover the generation of graphs from specific classes (namely split graphs and forests in this case)

A single degree sequence can have many graphs representing it. The problem of counting the number of graphs for a specific sequence is an open problem, but there is an upper bound that has been established. There are a couple of exhaustive methods that aim to generation multiple graphs satisfying the given degree sequence namely James Riha exhaustive and Kim exhaustive.

Sampling methods aim to sample a single graph from the space of all graphs for a given degree sequence. This comes in handy when the space increases for greater n values. Sampling has applications in analyzing network properties like degree assortativity and trait assortativity wherein it is crucial to generate a graph in the first place to represent the large sized networks. Similarly graphs of larger sizes would also need to be generated for the purpose of community detection. The above mentioned exhaustive methods have been modified to achieve sampling giving rise to James Riha sampling and Kim1sampling. Kim has a follow up sampling method that bas been modified with a binary search which is named as Kim2sampling. 
