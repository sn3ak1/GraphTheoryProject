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

    def from_file(self, name):
        matrix = []
        with open(name, 'r') as reader:
            for line in reader.readlines():
                matrix.append((line.strip()[:-1]).split(', '))
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if int(element) != 0:
                    start = 's' if i == 0 else i
                    end = 'e' if j == len(row)-1 else j
                    self.add_edge(start, end, int(element))


class Solver:
    def __init__(self, g):
        self.G = g
        self.max_flow = 0
        self.paths_taken = []

    def shortest_path(self):
        distance = {'s': 0}
        path = ['e']
        pending = [key for key in self.G['s'].successors.keys() if self.G['s'][key].remaining > 0]
        while len(pending):
            queue = pending
            pending = []
            for key in queue:
                distance[key] = min([distance[pred] for pred in self.G[key].predecessors.keys() if
                                     self.G[pred][key].remaining > 0 and pred in distance.keys()]) + 1
                keys = [x for x in self.G[key].successors.keys() if self.G[key][x].remaining > 0]
                if 'e' in keys:
                    pending = []
                    break
                pending += keys
        best = 'e'
        while best != 's':
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
        return list(zip(path, path[1:]))

    def flow_path(self, path):
        min_val = min(self.G[edge[0]][edge[1]].remaining for edge in path)
        self.max_flow += min_val
        for edge in path:
            self.G[edge[0]][edge[1]].remaining -= min_val

    def solve(self):
        self.paths_taken.append(self.shortest_path())
        while self.paths_taken[-1] is not None:
            self.flow_path(self.paths_taken[-1])
            self.paths_taken.append(self.shortest_path())
        del self.paths_taken[-1]


solver = Solver(Graph('data.txt'))
solver.solve()
print('Maximum flow: ' + str(solver.max_flow))
print('Paths taken: ' + str(solver.paths_taken))
