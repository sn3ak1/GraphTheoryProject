class Graph:
    class Edge:
        def __init__(self, capacity):
            self.capacity = capacity
            self.remaining = capacity

    class Node:
        def __init__(self, label):
            self.label = label
            self.predecessors = {}
            self.successors = {}

        def __getitem__(self, item):
            return self.successors[item]

    def __init__(self, import_from=None):
        self.nodes = {}
        if import_from is not None:
            self.from_file(import_from)

    def add_node(self, label):
        if not self.nodes.__contains__(label):
            self.nodes[label] = self.Node(label)

    def add_edge(self, start, end, capacity):
        edge = self.Edge(capacity)
        self.add_node(start)
        self.add_node(end)
        self.nodes[start].successors[end] = edge
        self.nodes[end].predecessors[start] = edge

    def __getitem__(self, item):
        return self.nodes[item]

    def is_directed(self, matrix):
        for i, _ in enumerate(matrix):
            for j, _ in enumerate(matrix[0]):
                if matrix[i][j] != matrix[j][i]:
                    return True
        return False

    def from_file(self, name):
        matrix = []
        with open(name, 'r') as reader:
            for line in reader.readlines():
                matrix.append((line.strip()[:-1]).split(', '))
        if not self.is_directed(matrix):
            raise Exception('Graph is undirected!')
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if int(element) != 0:
                    self.add_edge(i, j, int(element))


class Solver:
    def __init__(self, g):
        self.G = g
        self.max_flow = 0
        self.paths_taken = []

    def shortest_path(self, source, sink):
        distance = {source: 0}
        path = [sink]
        pending = [key for key in self.G[source].successors.keys() if self.G[source][key].remaining > 0]
        while len(pending):
            queue = pending
            pending = []
            for key in queue:
                distance[key] = min([distance[pred] for pred in self.G[key].predecessors.keys() if
                                    self.G[pred][key].remaining > 0 and pred in distance.keys()]) + 1
                keys = [x for x in self.G[key].successors.keys() if self.G[key][x].remaining > 0]
                if sink in keys:
                    pending = []
                    break
                pending += keys
        best = sink
        while best != source:
            predecessors = [pred for pred in self.G[best].predecessors.keys()
                            if self.G[pred][best].remaining > 0 and pred in distance.keys()]
            if not len(predecessors):
                return None
            best = predecessors[0]
            for pred in predecessors:
                if distance[pred] < distance[best]:
                    best = pred
            path.append(best)
        path.reverse()
        return list(map(list, zip(path, path[1:])))

    def flow_path(self, path):
        min_val = min(self.G[edge[0]][edge[1]].remaining for edge in path)
        self.max_flow += min_val
        for i, edge in enumerate(path):
            self.G[edge[0]][edge[1]].remaining -= min_val
            path[i].append(str(self.G[edge[0]][edge[1]].capacity-self.G[edge[0]][edge[1]].remaining)
                           + '/' + str(self.G[edge[0]][edge[1]].capacity))

    def solve(self, source, sink):
        if sink == -1:
            sink = len(self.G.nodes)-1
        if not self.G.nodes.__contains__(source) or not self.G.nodes.__contains__(sink):
            raise Exception('Graph doesn\'t contain node with specified index.')

        self.paths_taken.append(self.shortest_path(source, sink))
        while self.paths_taken[-1] is not None:
            self.flow_path(self.paths_taken[-1])
            self.paths_taken.append(self.shortest_path(source, sink))
        del self.paths_taken[-1]


try:
    source_input = input('Specify source node index (leave blank for 0): ')
except SyntaxError:
    source_input = ''
try:
    sink_input = input('Specify sink node index (leave blank for last node index): ')
except SyntaxError:
    sink_input = ''

solver = Solver(Graph('data.txt'))
solver.solve(int(source_input) if source_input != '' else 0, int(sink_input) if sink_input != '' else -1)
print('Maximum flow: ' + str(solver.max_flow))
print('Paths taken: ')
for path in solver.paths_taken:
    print(path)
