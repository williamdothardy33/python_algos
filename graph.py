# this is a vertex for an undirected connected graph
from queue_1 import queue
class vertex():
    data = None
    neighbors = {}
    def __init__(self, data):
        self.data = data

    def add_neighbor(self, vertex):
        if self.neighbors.get(vertex) is None:
            self.neighbors[vertex] = True
            vertex.add_neighbor(self)

def show(vertex):
    def dfs_show_recur(vertex, visited):
        if visited.get(vertex) is None:
            print(f'visited vertex: {vertex.data}')
            visited[vertex] = True
            for neighbor, _ in vertex.neighbors.items():
                dfs_show_recur(neighbor, visited)

    def bfs_show_iter(vertex):
        to_visit = queue()
        visited = {}
        to_visit.enqueue(vertex)
        while to_visit.not_empty():
            current = to_visit.dequeue()
            if visited.get(current) is None:
                print(f'visited vertex: {current.data}')
                visited[current] = True
                for neighbor, _ in current.neighbors.items():
                    to_visit.enqueue(neighbor)


    visited = {}
    #dfs_show_recur(vertex, visited)
    bfs_show_iter(vertex)



def test_vertex():
    alice = vertex('alice')
    bob = vertex('bob') 
    cynthia = vertex('cynthia')
    diana = vertex('diana')
    elise = vertex('elise')
    fred = vertex('fred')
    
    alice.add_neighbor(bob)
    alice.add_neighbor(diana)
    alice.add_neighbor(fred)
    bob.add_neighbor(alice)
    bob.add_neighbor(cynthia)
    bob.add_neighbor(diana)
    cynthia.add_neighbor(bob)
    diana.add_neighbor(alice)
    diana.add_neighbor(bob)
    diana.add_neighbor(fred)
    elise.add_neighbor(fred)
    fred.add_neighbor(alice)
    fred.add_neighbor(diana)
    fred.add_neighbor(elise)

    show(alice)
test_vertex()




