# ADJACENCY MATRIX GRAPH IMPLEMENTATION

class Graph:  # abstract base class, implemented below
    def __init__(self):  # when you initialize, these will just be empty lists
        self._numVerts = 0
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
    def getVertPosition(self):
        print(" the next value in the list is: " + self._next._element)
        print(" the previous value in the list" + self._prev._element)

    def getEdgePosition(self):
        print(" the next value in the list is: " + self._next.name())
        print(" the previous value in the list" + self._prev.name())


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
        return self._origin, self._end

    def opposite(self, v):  # given a vertex, find the other along this edge
        return self._end if v is self._origin else self._origin

    def name(self):  # returns a string representation of the edge in the format origin ---> end
        return Vertex.element(self._origin) + " ---> " + Vertex.element(self._end)


class GraphAM:
    def __init__(self):
        self.AM = []  # this is the adjacency Matrix. It will contain a grid of True/False values based on whether
        # edges exist.
        self._vertices = []
        self._numVerts = 0
        self._numEdges = 0

    def isDirected(self):
        return False

    def vertex_count(self):  # num of vertices
        return self._numVerts

    def vertices(self):  # prints out all vertices in the graph
        for vert in self._vertices:
            print(vert._element)

    def edge_count(self):  # num of edges
        return self._numEdges

    def edges(self):  # prints out all edges
        pos = 0
        for adjacent in self.AM:
            loc = 0
            for i in range(pos):  # basically, the idea here is to search exactly half the matrix. since this
                boolean = adjacent[i]  # is undirected, A <-> B exists, as well as B <-> A. we only want unique edges.
                if boolean is True:
                    print(self._vertices[pos]._element, "<--->", self._vertices[loc]._element)

                loc += 1
            pos += 1

    def addVertex(self, v):  # v being the new vertex
        if self._vertices:
            v._prev = self._vertices[len(self._vertices) - 1]  # add position pointers
            v._prev._next = v
        self._vertices.append(v)
        self._numVerts += 1

        for adjacent in self.AM:  # add new row and column to the matrix to accommodate new Vertex
            adjacent.append(False)
        newAdjList = []
        for i in range(len(self._vertices)):
            newAdjList.append(False)
        self.AM.append(newAdjList)

    def addEdge(self, u, v):  # u and v being vertices
        uPos = 0  # these loops find the coordinates of the edge in question
        for vert in self._vertices:
            if vert._element is u._element:
                break
            uPos += 1
        vPos = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
            vPos += 1

        self.AM[uPos][vPos] = True  # make the edge at the coords equal True
        self.AM[vPos][uPos] = True  # since this is undirected, there is an opposite connection
        self._numEdges += 1

    def removeVertex(self, v):  # v is vertex, removes v and all edges that have v as an endpoint
        loc = 0
        for vert in self._vertices:
            if vert._element is v._element:
                self._vertices.remove(vert)
                self._numVerts -= 1
                if vert._next and vert._prev:
                    vert._prev._next = vert._next  # adjust the pointers if necessary
                    vert._next._prev = vert._prev
                break
            loc += 1

        self.AM.__delitem__(loc)
        for adjacent in self.AM:
            if adjacent[loc] is True:
                pass
                self._numEdges -= 1
            adjacent.__delitem__(loc)

    def removeEdge(self, e):  # e is an edge, removes e without altering the vertices
        u = e._v1
        v = e._v2
        uPos = 0  # these loops find the coordinates of the edge in question
        for vert in self._vertices:
            if vert._element is u._element:
                break
            uPos += 1
        vPos = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
            vPos += 1

        self.AM[uPos][vPos] = False  # make the edge at the coords equal False
        self.AM[vPos][uPos] = False  # since this is undirected, there is an opposite connection
        self._numEdges -= 1

    def getEdge(self, u, v):
        upos = 0
        for vert in self._vertices:
            if vert._element is u._element:
                break
            upos += 1
        vpos = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
            vpos += 1
        bool = self.AM[upos][vpos]
        if bool:
            print(u._element, "<--->", v._element, "was found")
            return bool
        else:
            print(u._element, "<--->", v._element, "was not found")

    def degree(self, v):  # returns num of edges that contain vertex v
        degree = 0
        vloc = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
        adjacent = self.AM[vloc]
        for bool in adjacent:
            if bool:
                degree += 1
        return degree

    def incident_edges(self, v):  # prints out the edges that contain vertex v
        incident = []
        vloc = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
            vloc += 1
        adjacent = self.AM[vloc]
        for i in range(len(adjacent)):
            if adjacent[i] is True:
                edge = Edge(v, self._vertices[i])
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


class DiGraphAM:
    def __init__(self):
        self.AM = []  # this is the adjacency Matrix. It will contain a grid of True/False values based on whether
        # edges exist. the first value in each sublist going either vertically or horizontally is a vertex
        self._vertices = []  # v    v    v
        self._numVerts = 0  # v   T     F
        self._numEdges = 0  # v   F     T

    def isDirected(self):
        return True

    def vertex_count(self):  # num of vertices
        return self._numVerts

    def vertices(self):  # prints out all vertices in the graph
        for vert in self._vertices:
            print(vert._element)

    def edge_count(self):  # num of edges
        return self._numEdges

    def edges(self):  # prints out all edges
        pos = 0
        for adjacent in self.AM:
            loc = 0
            for boolean in adjacent:
                if boolean is True:
                    print(self._vertices[pos]._element, "--->", self._vertices[loc]._element)

                loc += 1
            pos += 1

    def addVertex(self, v):  # v being the new vertex
        if self._vertices:
            v._prev = self._vertices[len(self._vertices) - 1]  # add position pointers
            v._prev._next = v
        self._vertices.append(v)
        self._numVerts += 1

        for adjacent in self.AM:  # add new row and column to the matrix to accommodate new Vertex
            adjacent.append(False)
        newAdjList = []
        for i in range(len(self._vertices)):
            newAdjList.append(False)
        self.AM.append(newAdjList)

    def addEdge(self, u, v):  # u and v being vertices
        uPos = 0  # these loops find the coordinates of the edge in question
        for vert in self._vertices:
            if vert._element is u._element:
                break
            uPos += 1
        vPos = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
            vPos += 1

        self.AM[uPos][vPos] = True  # make the edge at the coords equal True
        self._numEdges += 1

    def removeVertex(self, v):  # v is vertex, removes v and all edges that have v as an endpoint
        loc = 0
        for vert in self._vertices:
            if vert._element is v._element:
                self._vertices.remove(vert)
                self._numVerts -= 1
                if vert._next and vert._prev:
                    vert._prev._next = vert._next  # adjust the pointers if necessary
                    vert._next._prev = vert._prev
                break
            loc += 1

        self.AM.__delitem__(loc)
        for adjacent in self.AM:
            if adjacent[loc] is True:
                self._numEdges -= 1
            adjacent.__delitem__(loc)

    def removeEdge(self, edge):  # e is an edge, removes e without altering the vertices
        u = edge._origin
        v = edge._end
        uPos = 0  # these loops find the coordinates of the edge in question
        for vert in self._vertices:
            if vert._element is u._element:
                break
            uPos += 1
        vPos = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
            vPos += 1

        self.AM[uPos][vPos] = False  # make the edge at the coords equal True
        self._numEdges -= 1

    def getEdge(self, u, v):
        upos = 0
        for vert in self._vertices:
            if vert._element is u._element:
                break
            upos += 1
        vpos = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
            vpos += 1
        bool = self.AM[upos][vpos]
        if bool:
            print(u._element, "--->", v._element, "was found")
            return bool
        else:
            print(u._element, "--->", v._element, "was not found")

    def degree(self, v):  # returns num of v's outgoing edges
        degree = 0
        vloc = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
            vloc += 1
        adjacent = self.AM[vloc]
        for bool in adjacent:
            if bool is True:
                degree += 1
        return degree

    def incident_edges(self, v):  # prints out the edges that contain vertex v
        incident = []
        vloc = 0
        for vert in self._vertices:
            if vert._element is v._element:
                break
            vloc += 1
        adjacent = self.AM[vloc]
        for i in range(len(adjacent)):
            if adjacent[i] is True:
                edge = DiEdge(v, self._vertices[i])
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


g = GraphAM()

evald = Vertex("Evald")
bennet = Vertex("Bennet")
bonnet = Vertex("Bonnet")
sampersand = Vertex("Sampersand")
freyja = Vertex("Freyja")
boogiebird = Vertex("Boogiebird")
boris = Vertex("Boris")
ambrose = Vertex("Ambrose")
fredericht = Vertex("Fredericht")

g.addVertex(evald)
g.addVertex(bennet)
g.addVertex(bonnet)
g.addVertex(sampersand)
g.addVertex(freyja)
g.addVertex(boogiebird)
g.addVertex(boris)
g.addVertex(ambrose)
g.addVertex(fredericht)

g.addEdge(bennet, bonnet)
g.addEdge(bennet, evald)
g.addEdge(evald, freyja)
g.addEdge(boris, bonnet)
g.addEdge(bennet, boogiebird)
g.addEdge(ambrose, freyja)
g.addEdge(evald, fredericht)

print("before deletion:")
print(g.vertex_count(), "vertices:")
g.vertices()
print()
print(g.edge_count(), "edges:")
g.edges()
print()

g.removeEdge(Edge(bennet, boogiebird))
g.removeEdge(Edge(bennet, bonnet))

g.removeVertex(bonnet)
g.removeVertex(fredericht)

print("after deletion:")
print(g.vertex_count(), "vertices:")
g.vertices()
print()
print(g.edge_count(), "edges:")
g.edges()
print()

g.getEdge(bennet, evald)
g.getEdge(ambrose, boris)

print()
print("degree of vertex evald:", g.degree(evald))
print("degree of vertex freyja:", g.degree(freyja))

print()
print("evald's incident edges:")
i = g.incident_edges(evald)
for incident in i:
    print(incident.name())
print()
print("freyja's incident edges:")
i = g.incident_edges(freyja)
for incident in i:
    print(incident.name())

print()
print("a depth first traversal discovers these vertices in order:")

g.addEdge(evald, bennet)  # add a few more edges to make things more interesting
g.addEdge(freyja, sampersand)
g.addEdge(freyja, boris)

d = g.dft(g._vertices[0])  # start at the root, which I have made as just the first vertex in the list
for vert in d:
    print(vert._element)

print()
g = DiGraphAM()

evald = Vertex("Evald")
bennet = Vertex("Bennet")
bonnet = Vertex("Bonnet")
sampersand = Vertex("Sampersand")
freyja = Vertex("Freyja")
boogiebird = Vertex("Boogiebird")
boris = Vertex("Boris")
ambrose = Vertex("Ambrose")
fredericht = Vertex("Fredericht")

g.addVertex(evald)
g.addVertex(bennet)
g.addVertex(bonnet)
g.addVertex(sampersand)
g.addVertex(freyja)
g.addVertex(boogiebird)
g.addVertex(boris)
g.addVertex(ambrose)
g.addVertex(fredericht)

g.addEdge(bennet, bonnet)
g.addEdge(bennet, evald)
g.addEdge(evald, freyja)
g.addEdge(boris, bonnet)
g.addEdge(bennet, boogiebird)
g.addEdge(ambrose, freyja)
g.addEdge(evald, fredericht)

print("before deletion:")
print(g.vertex_count(), "vertices:")
g.vertices()
print()
print(g.edge_count(), "edges:")
g.edges()
print()

g.removeEdge(DiEdge(bennet, boogiebird))
g.removeEdge(DiEdge(bennet, bonnet))

g.removeVertex(bonnet)
g.removeVertex(fredericht)

print("after deletion:")
print(g.vertex_count(), "vertices:")
g.vertices()
print()
print(g.edge_count(), "edges:")
g.edges()
print()

e = g.getEdge(bennet, evald)
e2 = g.getEdge(ambrose, boris)

print()
print("degree of vertex evald:", g.degree(evald))
print("degree of vertex freyja:", g.degree(freyja))

print()
print("evald's incident edges:")
i = g.incident_edges(evald)
for incident in i:
    print(incident.name())
print()
print("freyja's incident edges:")
i = g.incident_edges(freyja)
for incident in i:
    print(incident.name())

print()
print("a depth first traversal discovers these vertices in order:")

g.addEdge(evald, bennet)  # add a few more edges to make things more interesting (NOTE: this will affect the incident
g.addEdge(freyja, sampersand)  # edges of the nodes)
g.addEdge(freyja, boris)

d = g.dft(g._vertices[0])  # start at the root, which I have made as just the first vertex in the list
for vert in d:
    print(vert._element)
