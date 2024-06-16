# this is a vertex for an undirected connected graph
from queue_1 import queue
from min_priority_queue import min_priority_queue

def person(data):
    class person():
        data = None
        neighbors = {}

        def __init__(self, data):
            self.data = data

        def add_neighbor(self, vertex):
            self.neighbors[vertex] = True

        def show(self):
            return f'vertex data is: {self.data}'
    result = person(data)
    return result


def vertex(data):
    class vertex():
        data = None
        neighbors = {}
        def __init__(self, data):
            self.data = data

        def add_neighbor(self, vertex):
            if self.neighbors.get(vertex) is None:
                self.neighbors[vertex] = True
                vertex.add_neighbor(self)
    result = vertex(data)
    return result

def show(vertex):
    def dfs_show_recur(vertex, visited):
        print(f'visited vertex: {vertex.data}')
        visited[vertex] = True
        for neighbor, _ in vertex.neighbors.items():
            if visited.get(neighbor) is None:
                dfs_show_recur(neighbor, visited)

    def bfs_show_iter(vertex):
        to_visit = queue()
        visited = {}
        to_visit.enqueue(vertex)
        while to_visit.not_empty():
            print(f'current queue is: {to_visit.show()}')
            current = to_visit.dequeue()
            print(f'visited vertex: {current.data}')
            visited[current] = True
            for neighbor, _ in current.neighbors.items():
                if visited.get(neighbor) is None:
                    to_visit.enqueue(neighbor)


    visited = {}
    dfs_show_recur(vertex, visited)
    #bfs_show_iter(vertex)

# best to check before making recursive calls instead of checking after.
def search(data, start):
    def dfs_recur(data, current, visited):
        result = None
        visited[current] = True
        if current.data == data:
            result = current
        else:
            for neighbor, _ in current.neighbors.items():
                if visited.get(neighbor) is None:
                    result = dfs_recur(data, neighbor, visited)
                    if result is not None:
                        return result
        return result
    

    #check in loop cost much less than at the beginning of iteration because, queue gets filled with neighbors already visited potentially
    def bfs_iter(data, start):
        to_visit = queue()
        to_visit.enqueue(start)
        visited = {}

        while to_visit.not_empty() == True:
            current = to_visit.dequeue()
            visited[current] = True
            if current.data == data:
                return current
            else:
                for neighbor, _ in current.neighbors.items():
                    if visited.get(neighbor) is None:
                        to_visit.enqueue(neighbor)
    
    visited = {}
    #return dfs_recur(data, start, visited)
    return bfs_iter(data, start)

def shortest_path(origin, target):
    previous_origin = {}
    to_visit = min_priority_queue(0, origin)
    visited = {}
    cost = {origin: 0}

    while to_visit.not_empty():
        current = to_visit.dequeue()
        visited[current] = True
        for neighbor, _ in current.neighbors.items():
            if visited.get(neighbor) is None:
                current_cost = cost[current] + 1
                known_cost = cost.get(neighbor)
                if known_cost is not None:
                    if current_cost < known_cost:
                        to_visit.enqueue(current_cost, neighbor)
                        cost[neighbor] = current_cost
                        previous_origin[neighbor] = current
                    else:
                        continue
                else:
                    to_visit.enqueue(current_cost, neighbor)
                    cost[neighbor] = current_cost
                    previous_origin[neighbor] = current

    result = []
    current = target
    while current != origin:
        result.append(current.data)
        current = previous_origin[current]
        if current == origin:
            result.append(origin.data)
    result.reverse()
    return result
    
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

    #show(alice)
    found = search('elise', alice)
    print(f'vertex containing elise starting from alice is: {found}')
    print(f'value of found is: {found.data}')
#test_vertex()

def test_shortest_path():
    idris = person('idris')
    kamil = person('kamil')
    talia = person('talia')
    lina = person('lina')
    ken = person('ken')
    marco = person('marco')
    sasha = person('sasha')

    idris.add_neighbor(kamil)
    idris.add_neighbor(talia)
    kamil.add_neighbor(lina)
    talia.add_neighbor(ken)
    ken.add_neighbor(marco)
    marco.add_neighbor(sasha)
    sasha.add_neighbor(lina)

    result = shortest_path(idris, lina)

    print(f'the path from idris to lina is: {result}')

test_shortest_path()



