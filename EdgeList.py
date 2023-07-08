# EDGE LIST IMPLEMENTATION

class Graph:  # abstract base class, implemented below
    def __init__(self):  # when you initialize, these will just be empty lists
        self._numVerts = 0  # some variables to help keep track of the size of the lists
        self._numEdges = 0

    def isDirected(self):
        pass

    def vertex_count(self):  # num of vertices
        pass

    def vertices(self):  # prints out all vertices in the graph
        pass

    def edge_count(self):  # num of edges
        pass

    def edges(self):  # prints out all edges
        pass

    def addVertex(self, v):  # v being the new vertex
        pass

    def addEdge(self, u, v):  # u and v being vertices
        pass

    def removeVertex(self, v):  # v is vertex, removes v and all edges that have v as an endpoint
        pass

    def removeEdge(self, e):  # e is an edge, removes e without altering the vertices
        pass

    def getEdge(self, u, v):
        pass

    def degree(self, v):  # returns num of edges that contain vertex v
        pass

    def incident_edges(self, v):  # prints out the edges that contain vertex v
        pass


class Vertex:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, name):
        self._element = name
        self._next = None  # position relative to rest of graph
        self._prev = None

    def element(self):
        return self._element


class Position:  # position class
    def getVertPosition(self,v):
        print(" the next value in the list is: " + v._next._element)
        print(" the previous value in the list" + v._prev._element)

    def getEdgePosition(self,e):
        print(" the next value in the list is: " + e._next.name())
        print(" the previous value in the list" + e._prev.name())


class Edge:
    __slots__ = '_v1', '_v2', '_next', '_prev'

    def __init__(self, u, v):
        self._v1 = u
        self._v2 = v
        self._next = None  # position relative to rest of graph
        self._prev = None

    def vertices(self):  # gives a tuple of the vertices
        return (self._v1, self._v2)

    def opposite(self, v):  # given a vertex, find the other along this edge
        return self._v2 if v is self._v1 else self._v1

    def name(self):  # returns a string representation of the edge in the format v1 <---> v2
        return Vertex.element(self._v1) + " <---> " + Vertex.element(self._v2)


class DiEdge:
    __slots__ = '_origin', '_end', '_next', '_prev'

    def __init__(self, u, v):
        self._origin = u
        self._end = v
        self._next = None  # position relative to rest of graph
        self._prev = None

    def vertices(self):  # gives a tuple of the vertices
        return (self._origin, self._end)

    def opposite(self, v):  # given a vertex, find the other along this edge
        return self._end if v is self._origin else self._origin

    def name(self):  # returns a string representation of the edge in the format origin ---> end
        return Vertex.element(self._origin) + " ---> " + Vertex.element(self._end)


class GraphEL(Graph):
    def __init__(self):  # when you initialize, these will just be empty lists
        super().__init__()
        self._vertices = []
        self._edges = []
        self._lenVertices = 0
        self._lenEdges = 0

    def isDirected(self):  # manually set to false
        return False

    def vertex_count(self):  # num of vertices
        return self._lenVertices

    def vertices(self):  # prints out all vertices in the graph
        for vert in self._vertices:
            print(vert._element)
        return self._vertices

    def edge_count(self):  # num of edges
        return self._lenEdges

    def edges(self):  # prints out all edges
        for edge in self._edges:
            print(edge.name())
        return self._edges

    def addVertex(self, v):  # v being the new vertex
        if self._vertices:  # establish a position relative to the rest of the nodes
            v._prev = self._vertices[
                self._lenVertices - 1]  # in terms of position, the previous of the current is at the end
            v._prev._next = v  # establish a "next"      # of the list
        self._vertices.append(v)  # is new root
        self._lenVertices += 1  # finally, increment the length

    def addEdge(self, u, v):  # u and v being vertices
        edge = Edge(u, v)
        if self._edges:
            edge._prev = self._edges[self._lenEdges - 1]
            edge._prev._next = edge
        self._edges.append(edge)
        self._lenEdges += 1

    # this works well with an edge list. Not so much with the position pointers. I've had some trouble getting the beginning
    # and end elements to link their pointers to the rest of the graph correctly
    def removeVertex(self, v):  # v is vertex, removes v and all edges that have v as an endpoint
        for vert in self._vertices:
            if vert._element is v._element:
                if vert._next and vert._prev:
                    vert._prev._next = vert._next  # adjust the pointers
                    vert._next._prev = vert._prev
                for edge in self._edges:  # remove all traces of the vertex. even from edge list
                    if edge._v1._element is v._element or edge._v2._element is v._element:
                        if edge._next and edge._prev:
                            edge._prev._next = edge._next  # adjust the pointers
                            edge._next._prev = edge._prev
                        self._edges.remove(edge)  # remove edges from the list
                        self._lenEdges -= 1
                self._vertices.remove(vert)  # remove from the list
                self._lenVertices -= 1

    def removeEdge(self, e):  # e is an edge, removes e without altering the vertices
        for edge in self._edges:
            if (edge._v2._element is e._v2._element and edge._v1._element is e._v1._element) or (
                    edge._v1._element is e._v2._element and edge._v2._element is e._v1._element):
                if edge._next and edge._prev:
                    edge._prev._next = edge._next  # adjust the pointers
                    edge._next._prev = edge._prev
                self._edges.remove(edge)  # remove edges from the list
                self._lenEdges -= 1

    def getEdge(self, u, v):
        for edge in self._edges:
            if edge._v2._element is u._element and edge._v1._element is v._element:
                return edge
            elif edge._v2._element is v._element and edge._v1._element is u._element:  # edge could go the other way, too
                return edge
        print(u._element + "<--->" + v._element + " does not exist")

    def degree(self, v):  # returns num of edges that contain vertex v
        deg = 0
        for edge in self._edges:
            if v._element is edge._v2._element or v._element is edge._v1._element:
                deg += 1
        return deg

    def incident_edges(self, v):  # prints out the edges that contain vertex v
        incident = []
        for edge in self._edges:
            if v._element is edge._v2._element or v._element is edge._v1._element:
                incident.append(edge)
        return incident

    def dft(self, v, discovered=dict()):  # Depth First Traversal; recursive search
        if v not in discovered:
            discovered[v] = None
        for e in self.incident_edges(v):
            u = e.opposite(v)
            if u not in discovered:
                discovered[u] = e
                self.dft(u, discovered)
        return discovered


class DiGraphEL(Graph):
    def __init__(self):  # when you initialize, these will just be empty lists
        super().__init__()
        self._vertices = []
        self._edges = []
        self._lenVertices = 0
        self._lenEdges = 0

    def isDirected(self):  # manually set to false
        return False

    def vertex_count(self):  # num of vertices
        return self._lenVertices

    def vertices(self):  # prints out all vertices in the graph
        for vert in self._vertices:
            print(vert._element)
        return self._vertices

    def edge_count(self):  # num of edges
        return self._lenEdges

    def edges(self):  # prints out all edges
        for edge in self._edges:
            print(edge.name())
        return self._edges

    def addVertex(self, v):  # v being the new vertex
        if self._vertices:  # establish a position relative to the rest of the nodes
            v._prev = self._vertices[
                self._lenVertices - 1]  # in terms of position, the previous of the current is at the end
            v._prev._next = v  # establish a "next"      # of the list
        self._vertices.append(v)  # is new root
        self._lenVertices += 1  # finally, increment the length

    def addEdge(self, u, v):  # u and v being vertices
        edge = DiEdge(u, v)
        if self._edges:
            edge._prev = self._edges[self._lenEdges - 1]
            edge._prev._next = edge
        self._edges.append(edge)
        self._lenEdges += 1

    # this works well with an edge list. Not so much with the position pointers. I've had some trouble getting the beginning
    # and end elements to link their pointers to the rest of the graph correctly
    def removeVertex(self, v):  # v is vertex, removes v and all edges that have v as an endpoint
        for vert in self._vertices:
            if vert._element is v._element:
                if vert._next and vert._prev:
                    vert._prev._next = vert._next  # adjust the pointers
                    vert._next._prev = vert._prev
                for edge in self._edges:  # remove all traces of the vertex. even from edge list
                    if edge._origin._element is v._element or edge._end._element is v._element:
                        if edge._next and edge._prev:
                            edge._prev._next = edge._next  # adjust the pointers
                            edge._next._prev = edge._prev
                        self._edges.remove(edge)  # remove edges from the list
                        self._lenEdges -= 1
                self._vertices.remove(vert)  # remove from the list
                self._lenVertices -= 1

    def removeEdge(self, e):  # e is an edge, removes e without altering the vertices
        ecopy = DiEdge(e._end, e._origin)
        for edge in self._edges:
            if (edge._end._element is e._end._element and edge._origin._element is e._origin._element) or \
                    (edge._origin._element is e._end._element and edge._end._element is e._origin._element):
                if edge._next and edge._prev:
                    edge._prev._next = edge._next  # adjust the pointers
                    edge._next._prev = edge._prev
                self._edges.remove(edge)  # remove edges from the list
                self._lenEdges -= 1

    def getEdge(self, u, v):
        for edge in self._edges:
            if edge._origin._element is u._element and edge._end._element is v._element:
                return edge
        print(u._element + "--->" + v._element + " does not exist")

    def degree(self, v):  # returns num of outgoing edges that contain vertex v
        deg = 0
        for edge in self._edges:
            if v._element is edge._origin._element:
                deg += 1
        return deg

    def incident_edges(self, v):  # prints out the outgoing edges that contain vertex v
        incident = []
        for edge in self._edges:
            if v._element is edge._origin._element:
                incident.append(edge)
        return incident

    def dft(self, v, discovered=dict()):  # algorithm found in slides
        if v not in discovered:
            discovered[v] = None
        for e in self.incident_edges(v):
            u = e.opposite(v)
            if u not in discovered:
                discovered[u] = e
                self.dft(u, discovered)
        return discovered

# TESTING
pets = GraphEL()

evald = Vertex("Evald")
bennet = Vertex("Bennet")
bonnet = Vertex("Bonnet")
sampersand = Vertex("Sampersand")
freyja = Vertex("Freyja")
boogiebird = Vertex("Boogiebird")
boris = Vertex("Boris")
ambrose = Vertex("Ambrose")
fredericht = Vertex("Fredericht")

pets.addVertex(evald)
pets.addVertex(bennet)
pets.addVertex(bonnet)
pets.addVertex(sampersand)
pets.addVertex(freyja)
pets.addVertex(boogiebird)
pets.addVertex(boris)
pets.addVertex(ambrose)
pets.addVertex(fredericht)

pets.addEdge(bennet, bonnet)
pets.addEdge(bennet, evald)
pets.addEdge(evald, freyja)
pets.addEdge(boris, bonnet)
pets.addEdge(bennet, boogiebird)
pets.addEdge(ambrose, freyja)
pets.addEdge(evald, fredericht)

print("before deletion:")
print(pets.vertex_count(), "vertices:")
pets.vertices()
print()
print(pets.edge_count(), "edges:")
pets.edges()
print()

pets.removeEdge(Edge(bennet, boogiebird))
pets.removeEdge(Edge(bennet, bonnet))

pets.removeVertex(bonnet)
pets.removeVertex(fredericht)

print("after deletion:")
print(pets.vertex_count(), "vertices:")
pets.vertices()
print()
print(pets.edge_count(), "edges:")
pets.edges()
print()

pets.getEdge(bennet, evald)
pets.getEdge(ambrose, boris)

print()
print("degree of vertex evald:", pets.degree(evald))
print("degree of vertex freyja:", pets.degree(freyja))

print()
print("evald's incident edges:")
i = pets.incident_edges(evald)
for incident in i:
    print(incident.name())
print()
print("freyja's incident edges:")
i = pets.incident_edges(freyja)
for incident in i:
    print(incident.name())

print()
print("a depth first traversal discovers these vertices in order:")

pets.addEdge(evald, bennet)  # add a few more edges to make things more interesting
pets.addEdge(freyja, sampersand)
pets.addEdge(freyja, boris)

d = pets.dft(pets._vertices[0])  # start at the root, which I have made as just the first vertex in the list
for vert in d:
    print(vert._element)

print()
pets = DiGraphEL()

evald = Vertex("Evald")
bennet = Vertex("Bennet")
bonnet = Vertex("Bonnet")
sampersand = Vertex("Sampersand")
freyja = Vertex("Freyja")
boogiebird = Vertex("Boogiebird")
boris = Vertex("Boris")
ambrose = Vertex("Ambrose")
fredericht = Vertex("Fredericht")

pets.addVertex(evald)
pets.addVertex(bennet)
pets.addVertex(bonnet)
pets.addVertex(sampersand)
pets.addVertex(freyja)
pets.addVertex(boogiebird)
pets.addVertex(boris)
pets.addVertex(ambrose)
pets.addVertex(fredericht)

pets.addEdge(bennet, bonnet)
pets.addEdge(bennet, evald)
pets.addEdge(evald, freyja)
pets.addEdge(boris, bonnet)
pets.addEdge(bennet, boogiebird)
pets.addEdge(ambrose, freyja)
pets.addEdge(evald, fredericht)

print("before deletion:")
print(pets.vertex_count(), "vertices:")
pets.vertices()
print()
print(pets.edge_count(), "edges:")
pets.edges()
print()

pets.removeEdge(DiEdge(bennet, boogiebird))
pets.removeEdge(DiEdge(bennet, bonnet))

pets.removeVertex(bonnet)
pets.removeVertex(fredericht)

print("after deletion:")
print(pets.vertex_count(), "vertices:")
pets.vertices()
print()
print(pets.edge_count(), "edges:")
pets.edges()
print()

e = pets.getEdge(bennet, evald)
e2 = pets.getEdge(ambrose, boris)

print()
print("degree of vertex evald:", pets.degree(evald))
print("degree of vertex freyja:", pets.degree(freyja))

print()
print("evald's incident edges:")
i = pets.incident_edges(evald)
for incident in i:
    print(incident.name())
print()
print("freyja's incident edges:")
i = pets.incident_edges(freyja)
for incident in i:
    print(incident.name())

print()
print("a depth first traversal discovers these vertices in order:")

pets.addEdge(evald, bennet)  # add a few more edges to make things more interesting (NOTE: this will affect the incident
pets.addEdge(freyja, sampersand)  # edges of the nodes)
pets.addEdge(freyja, boris)

d = pets.dft(pets._vertices[0])  # start at the root, which I have made as just the first vertex in the list
for vert in d:
    print(vert._element)

