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

    result = dijkstra(atlanta, denver)

    print(f'min price from atlanta to denver is: {result.cost}')
    print(f'the route from atlanta to denver is: {result.path}')
    

test_dijkstra()