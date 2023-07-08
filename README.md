# GraphImplementation
Python Implementation of Graph and Directed Graph. Includes Edge/Adjacency List and Adjacency Matrix versions

prerequisites:
* Python 3.8 (https://www.python.org/downloads/)

Contains:
3 files, each a separate implementation of Graph and Directed Graph concepts: AdjacencyList2.py, AdjacencyMatrix.py, EdgeList.py
1 main file, which includes abstract base Graph/Digraph classes: main.py

AdjacencyList2.py uses an adjacency list to store vertices, meaning each vertex has a list of vertices it is connected to.
AdjacencyMatrix.py uses a matrix of True/False values to show the connections between various vertices.
EdgeList.py uses a list of vertex positions relative to the rest of the graph, introducing a sort of order to the vertices. 

Conceptual Information:
A Graph is a set of connected nodes (also known as vertices). Each vertex can be connected to any number of other vertices, including zero vertices, by edges. In a standard graph, these connections are bidirectional, meaning they can be traversed in both directions. In a Directed Graph (DiGraph), these connections only go one way, meaning traversals can be more difficult. A vertex's incident edges are the edges that are connected to that vertex. A vertex's degree is the number of edges that vertex has. The Root of the graph is the first vertex. Please note that the AdjacencyList2.py, AdjacencyMatrix.py, and EdgeList.py files have implementations of a depth first search, a traversal algorithm specifically designed for graphs. For more information on Depth First Searches, see (https://en.wikipedia.org/wiki/Depth-first_search)

Run Instructions:
Copy any files to local machine and run python code using the following command (Windows):
python3 (file.py)
This will print the hard coded test data as an implementation of a Graph/Directed Graph. As it stands, this data displays a network of pets. Some pets know each other (represented by edges), others do not. This creates a net or spiderweb like structure of relationships.
