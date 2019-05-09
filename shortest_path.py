from collections import defaultdict, deque
import time

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

#function implementing Dijkstra algorithm using a single source node
#calling variable visited to the initial source node equal to 0
#line-27 sets up path as an empty dictionary for the shortest path
#line-29 nodes variable sets() up a pytjon set and returns it
#if statements inside a while loop will run setting up node to min_node
#by comparing the visited nodes' to the already visited current min_node and return the min_node

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    destination_ = paths[destination]

    while destination_ != origin:
        full_path.appendleft(destination_ )
        destination_ = paths[destination_ ]

    full_path.appendleft(origin)
   
    full_path.append(destination)

    return visited[destination], list(full_path)

########## Main Program ##########
if __name__ == '__main__':
    graph = Graph()

    nodelist = ['San Jose', 'Milpitas', 'Mountain View', 'Fremont', 'Palo Alto', 'Hayward', 'South SF']
    for node in nodelist:
        graph.add_node(node)
       

var = 1
while var == 1:
    print('Where would you like to go?\n1: Milpitas\n2: Mountain View\n3: Fremont\n4: Palo Alto\n5: Hayward')
    user = input('6: South SF\nDestination: ')
    try:
        if int(user[0]) < 1 or int(user[0]) > 6:
            print('That is not a valid destination\n')
            continue
    except:
        if user not in nodelist:
            print('That is not a valid destination\n')
            continue

    user1 = input('Will you be [D]riving, taking the [B]us or the [T]rain?\n')

    if user1[0] in {'d', 'D'}:
        graph.add_edge('San Jose', 'Milpitas', 16)
        graph.add_edge('San Jose', 'Mountain View', 19)
        graph.add_edge('Milpitas', 'Fremont', 16)
        graph.add_edge('Mountain View', 'Fremont', 25)
        graph.add_edge('Milpitas', 'Palo Alto', 19)
        graph.add_edge('Fremont', 'Palo Alto', 25)
        graph.add_edge('Palo Alto', 'Hayward', 40)
        graph.add_edge('Hayward', 'South SF', 33)
        graph.add_edge('Palo Alto', 'South SF', 26)

    elif user1[0] in {'b', 'B'}:
        graph.add_edge('San Jose', 'Milpitas', 23)
        graph.add_edge('San Jose', 'Mountain View', 49)
        graph.add_edge('Milpitas', 'Fremont', 62)
        graph.add_edge('Mountain View', 'Fremont', 120)
        graph.add_edge('Milpitas', 'Palo Alto', 135)
        graph.add_edge('Fremont', 'Palo Alto', 180)
        graph.add_edge('Palo Alto', 'Hayward', 240)
        graph.add_edge('Hayward', 'South SF', 152)
        graph.add_edge('Palo Alto', 'South SF', 96)

    elif user1[0] in {'t', 'T'}:
        graph.add_edge('San Jose', 'Milpitas', 42)
        graph.add_edge('San Jose', 'Mountain View', 100)
        graph.add_edge('Milpitas', 'Fremont', 55)
        graph.add_edge('Mountain View', 'Fremont', 100)
        graph.add_edge('Milpitas', 'Palo Alto', 90)
        graph.add_edge('Fremont', 'Palo Alto', 67)
        graph.add_edge('Palo Alto', 'Hayward', 110)
        graph.add_edge('Hayward', 'South SF', 71)
        graph.add_edge('Palo Alto', 'South SF', 44)

    else:
        print('That is not a valid transport type\n')
        continue

    start_time = time.time()
    print("The quickest route: ")
    try:
        print(shortest_path(graph, 'San Jose', nodelist[int(user[0])]))
    except:
        print(shortest_path(graph, 'San Jose', user))
    print("--- Running Time %s seconds ---" % (time.time() - start_time))
    input()
