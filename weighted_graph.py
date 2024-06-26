#comment so I can re commit with appropriate message
from min_priority_queue import min_priority_queue

def wd_vertex(data):
    class wd_vertex():
        data = None
        neighbors = {}
        path = []
        cost = None

        def __init__(self, data):
            self.data = data

        def add_neighbor(self, vertex, weight):
            self.neighbors[vertex] = weight

        def show(self):
            return f'vertex data is: {self.data}'
    result = wd_vertex(data)
    return result


#in the following a vertex in visited means that path suffixes from the vertex have been explored
#ok here is my take on dijkstra because I think I misunderstood it. according to my interpretation of the wiki,
#the primary purpose of the while loop in the wiki implementation is to update the tables for vertices that
#haven't been visited yet, while the while loop below is used to queue up path suffixes from a neighbor vertex to explore. ultimately, putting it into words
#the wiki dijkstra says: Do not update tables for neighbor vertices for 'this' path prefix if those vertices have already been visited and if they haven't been visited
#only update tables using this path prefix if it's 'shorter' than any known path prefix
# (presumably if they've already been visited the minimum path prefix leading to that neighbor vertex has already been found and recorded in the tables) 
# and do not advance from vertices that have already been visited (aka do not explore path suffixes that have already been explored). The below implementation says: 
# do not explore from neighbor vertices using this path prefix if there is a known path prefix to that neighbor vertex that is shorter 
# than this one (aka only use the smallest path prefix), nor update values
# for neighbor vertices in the table and do not advance from vertices that have already been visited 
# (in other words only explore path suffixes from this vertex if not explored already). the below implementation specifies a condition of traversal, constrained
# to 'minimum path' prefix out of all path prefixes that lead to a particular vertex, while the wiki dijkstra specifies a condition for when to do table writes
# constrained by a decreasing set of unvisited vertices

#dijkstra is just bfs with a twist
def dijkstra(origin, target):
    min_weights_from_origin = {origin: 0}
    previous_origin = {}
    visited = {}
    to_visit = min_priority_queue(0, origin)

    while to_visit.not_empty() == True:
        current = to_visit.dequeue()
        if visited.get(current) is None:
            visited[current] = True
            for neighbor, weight in current.neighbors.items():
                if visited.get(neighbor) is None:
                    current_weight = min_weights_from_origin.get(current) + weight
                    known_weight = min_weights_from_origin.get(neighbor)
                    if known_weight is not None:
                        if current_weight < known_weight:
                            to_visit.enqueue(current_weight, neighbor)
                            min_weights_from_origin[neighbor] = current_weight
                            previous_origin[neighbor] = current
                        else:
                            continue
                    else:
                        to_visit.enqueue(current_weight, neighbor)
                        min_weights_from_origin[neighbor] = current_weight
                        previous_origin[neighbor] = current

    origin.cost = min_weights_from_origin[target]
    current = target
    while current != origin:
        origin.path.append(current.data)
        current = previous_origin[current]
        if current == origin:
            origin.path.append(current.data)
            break

    origin.path.reverse()

    return origin

def test_dijkstra():
    denver = wd_vertex('denver')
    chicago = wd_vertex('chicago')
    boston = wd_vertex('boston')
    el_paso = wd_vertex('el paso')
    atlanta = wd_vertex('atlanta')

    denver.add_neighbor(chicago, 40)
    denver.add_neighbor(el_paso, 140)

    chicago.add_neighbor(el_paso, 80)

    boston.add_neighbor(chicago, 120)
    boston.add_neighbor(denver, 180)

    el_paso.add_neighbor(boston, 100)

    atlanta.add_neighbor(denver, 160)
    atlanta.add_neighbor(boston, 100)

    result = dijkstra(atlanta, el_paso)

    print(f'min price from atlanta to el paso is: {result.cost}')
    print(f'the route from atlanta to el paso is: {result.path}')
    

test_dijkstra()