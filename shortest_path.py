from collections import defaultdict, deque



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
       destination_  = paths[destination_ ]

   full_path.appendleft(origin)
   
   full_path.append(destination)

   return visited[destination], list(full_path)

if __name__ == '__main__':
   graph = Graph()

   for node in ['San Jose', 'Milpitas', 'Mountain View', 'Fremont', 'Palo Alto', 'Hayward', 'South SF']:
       graph.add_node(node)
       

var=1
while var==1:
   user=input('Where would you like to go?\n1: Milpitas\n2: Mountain View\n3: Fremont\n4: Palo Alto\n5: Hayward\n6: South SF\nDestination: ')
   user1= input('Will you be [D]riving, taking the [B]us or the [T]rain?\n')

   if user1[0] in {'d', 'D'}:
    graph.add_edge('San Jose', 'Milpitas', 10)
    graph.add_edge('San Jose', 'Mountain View', 20)
    graph.add_edge('Milpitas', 'Fremont', 15)
    graph.add_edge('Mountain View', 'Fremont', 30)
    graph.add_edge('Milpitas', 'Palo Alto', 50)
    graph.add_edge('Fremont', 'Palo Alto', 30)
    graph.add_edge('Palo Alto', 'Hayward', 5)
    graph.add_edge('Hayward', 'South SF', 2)

    #print(shortest_path(graph, 'San Jose', user))

   elif user1[0] in {'b', 'B'}:
        graph.add_edge('San Jose', 'Milpitas', 10)
        graph.add_edge('San Jose', 'Mountain View', 20)
        graph.add_edge('Milpitas', 'Fremont', 15)
        graph.add_edge('Mountain View', 'Fremont', 30)
        graph.add_edge('Milpitas', 'Palo Alto', 60)
        graph.add_edge('Fremont', 'Palo Alto', 40)
        graph.add_edge('Palo Alto', 'Hayward', 5)
        graph.add_edge('Hayward', 'South SF', 2)

        #print(shortest_path(graph, 'San Jose', user))
   elif user1[0] in {'t', 'T'}:
        graph.add_edge('San Jose', 'Milpitas', 10)
        graph.add_edge('San Jose', 'Mountain View', 20)
        graph.add_edge('Milpitas', 'Fremont', 15)
        graph.add_edge('Mountain View', 'Fremont', 30)
        graph.add_edge('Milpitas', 'Palo Alto', 60)
        graph.add_edge('Fremont', 'Palo Alto', 40)
        graph.add_edge('Palo Alto', 'Hayward', 5)
        graph.add_edge('Hayward', 'South SF', 2)

   else:
       print('That is not a valid input')
       continue

   print(shortest_path(graph, 'San Jose', user))


