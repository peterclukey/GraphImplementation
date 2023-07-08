
class Graph:  # abstract base class, implemented below
    def __init__(self):  # when you initialize, these will just be empty lists
        self._vertices = []
        self._edges = []

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
        self._next = None  # position
        self._prev = None

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))


class Edge:
    __slots__ = '_v1', '_v2'

    def __init__(self, u, v):
        self._v1 = u
        self._v2 = v

    def vertices(self):  # gives a tuple of the vertices
        return (self._v1, self._v2)

    def opposite(self, v):  # given a vertex, find the other along this edge
        return self._v2 if v is self._v1 else self._v1

    def name(self):  # returns a string representation of the edge in the format v1 <---> v2
        return Vertex.element(self._v1) + " <---> " + Vertex.element(self._v2)


class DiEdge:
    __slots__ = '_origin', '_end'

    def __init__(self, u, v):
        self._origin = u
        self._end = v

    def vertices(self):  # gives a tuple of the vertices
        return (self._origin, self._end)

    def opposite(self, v):  # given a vertex, find the other along this edge
        return self._end if v is self._origin else self._origin

    def name(self):  # returns a string representation of the edge in the format origin ---> end
        return Vertex.element(self._origin) + " ---> " + Vertex.element(self._end)


# Implementations for Graph abstract class. I decided I wanted both Digraph and Graph to implement the same
# abstract base class, since they share many of the same methods and differ only in a few minor areas.
#
# Please note that the "position" class is implemented inside the Vertex class above as the
# _element data member. Basically, each node/vertex (and edge for that matter) has its own distinct name, _element,
# much of the comparisons in the search and deletion methods use this element uniqueness to find certain conditions
# and edges

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
        return len(self._vertices)

    def vertices(self):  # prints out all vertices in the graph
        for i in self._vertices:
            print(i.element())

    def edge_count(self):  # num of edges
        return len(self._edges)

    def edges(self):  # prints out all edges
        for i in self._edges:
            print(i.name())

    def addVertex(self, v):  # v being the new vertex
        if self._vertices:  # establish a position relative to the rest of the nodes
            v._prev = self._vertices[
                len(self._vertices) - 1]  # in terms of position, the previous of the current is at the end
            v._prev._next = v  # establish a "next"      # of the list
        self._vertices.append(v)
        self._lenVertices += 1

    def addEdge(self, u, v):  # u and v being vertices
        e = Edge(u, v)  # make a new edge object
        self._edges.append(e)
        self._lenEdges += 1

    def removeVertex(self, v):  # v is vertex, removes v and all edges that have v as an endpoint
        for vert in self._vertices:
            if vert._element == v._element:
                if vert._prev:
                    vert._prev._next = vert._next  # alter the positions
                if vert._next:
                    vert._next._prev = vert._prev
                self._vertices.remove(vert)

        for edge in self._edges:
            if edge._v1._element == v._element or edge._v2._element == v._element:
                self._edges.remove(edge)
                self._lenEdges -= 1
        self._lenVertices -= 1

    def removeEdge(self, e):  # e is an edge, removes e without altering the vertices
        for edge in self._edges:
            if edge == e:
                self._vertices.remove(edge)
                self._lenEdges -= 1

    def getEdge(self, u, v):
        for edge in self._edges:
            if edge._v2._element is u._element and edge._v1._element is v._element:
                return edge
            elif edge._v2._element is v._element and edge._v1._element is u._element:  # edge could go the other way, too
                return edge
        print("no such element exists")

    def degree(self, v):  # returns num of edges that contain vertex v
        deg = 0
        for edge in self._edges:
            if v._element is edge._v2._element or v._element is edge._v1._element:
                deg += 1
        return deg

    def incident_edges(self, v):  # prints out the edges that contain vertex v
        for edge in self._edges:
            if v._element is edge._v2._element or v._element is edge._v1._element:
                print(edge.name())


class DiGraphEL(Graph):  #Directed Graph (Edge List)
    def __init__(self):  # when you initialize, these will just be empty lists
        super().__init__()
        self._vertices = []
        self._edges = []
        self._lenVertices = 0
        self._lenEdges = 0

    def isDirected(self):  # manually set to true
        return True

    def vertex_count(self):  # num of vertices
        return self._lenVertices

    def vertices(self):  # prints out all vertices in the graph
        for i in self._vertices:
            print(i.element())

    def edge_count(self):  # num of edges
        return self._lenEdges

    def edges(self):  # prints out all edges
        for i in self._edges:
            print(i.name())

    def addVertex(self, v):  # v being the new vertex
        if self._vertices:  # establish a position relative to the rest of the nodes
            v._prev = self._vertices[
                len(self._vertices) - 1]  # in terms of position, the previous of the current is at the end
            v._prev._next = v  # establish a "next"      # of the list
        self._vertices.append(v)
        self._lenVertices += 1

    def addEdge(self, u, v):  # u and v being vertices
        e = DiEdge(u, v)  # make a new di-edge object
        self._edges.append(e)
        self._lenEdges += 1

    def removeVertex(self, v):  # v is vertex, removes v and all edges that have v as an endpoint
        for vert in self._vertices:
            if vert._element == v._element:
                self._vertices.remove(vert)
                if vert._prev:
                    vert._prev._next = vert._next  # alter the positions
                if vert._next:
                    vert._next._prev = vert._prev
        for edge in self._edges:
            if edge._origin._element == v._element or edge._end._element == v._element:
                self._edges.remove(edge)
                self._lenEdges -= 1
        self._lenVertices -= 1

    def removeEdge(self, e):  # e is an edge, removes e without altering the vertices
        for edge in self._edges:
            if edge == e:
                self._edges.remove(edge)
                self._lenEdges -= 1

    def getEdge(self, u, v):
        for edge in self._edges:
            if edge._end._element is v._element and edge._origin._element is u._element:
                return edge
        print("no such element exists")
        return None

    def degree(self, v):  # returns num of edges that contain vertex v
        deg = 0
        for edge in self._edges:
            if v._element is edge._origin._element:
                deg += 1
        return deg

    def incident_edges(self, v):  # prints out the edges that contain vertex v
        for edge in self._edges:
            if v._element is edge._origin._element:
                print(edge.name())

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

pets.removeEdge(Edge(Vertex("Bennet"), Vertex("BoogieBird")))
pets.removeEdge(Edge(Vertex("Bennet"), Vertex("Bonnet")))

pets.removeVertex(Vertex("Bonnet"))
pets.removeVertex(Vertex("Fredericht"))

print("number of vertices: ", pets.vertex_count())
print("vertices:")
pets.vertices()
print()
print("number of edges", pets.edge_count())
print("edges: ")
pets.edges()
print()

print("Edge between Bennet and Evald?")
e = pets.getEdge(Vertex("Bennet"), Vertex("Evald"))
if e is not None:
    print(e.name())

print("Edge between Ambrose and Boris?")
e2 = pets.getEdge(Vertex("Ambrose"), Vertex("Boris"))
if e2 is not None:
    print(e2.name())
print()
print("Evald's degree: ", pets.degree(evald))
print("Freyja's degree: ", pets.degree(freyja))

print("Evald's incident edges: ")
pets.incident_edges(evald)
print("Freyja's incident edges: ")
pets.incident_edges(freyja)
print()
print("graph loaded and tested successfully")
print()
print("testing DiGraph")
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

pets.removeEdge(DiEdge(Vertex("Bennet"), Vertex("BoogieBird")))
pets.removeEdge(DiEdge(Vertex("Bennet"), Vertex("Bonnet")))

pets.removeVertex(Vertex("Bonnet"))
pets.removeVertex(Vertex("Fredericht"))

print("number of vertices: ", pets.vertex_count())
print("vertices:")
pets.vertices()
print()
print("number of edges", pets.edge_count())
print("edges: ")
pets.edges()
print()

print("Edge between Bennet and Evald?")
e = pets.getEdge(Vertex("Bennet"), Vertex("Evald"))
if e is not None:
    print(e.name())

print("Edge between Ambrose and Boris?")
e2 = pets.getEdge(Vertex("Ambrose"), Vertex("Boris"))
if e2 is not None:
    print(e2.name())
print()
print("Evald's degree: ", pets.degree(evald))
print("Freyja's degree: ", pets.degree(freyja))

print("Evald's incident edges: ")
pets.incident_edges(evald)
print("Freyja's incident edges: ")
pets.incident_edges(freyja)

print("Digraph loaded and tested successfully")
