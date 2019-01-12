# Minimal network
# Problem 107

import logging
logger = logging.getLogger('p107')
from copy import deepcopy

class Network:
    def __init__(self, matrix):
        self.matrix = matrix
        self.num_vertice = len(matrix)
        self.vertice = [0]*self.num_vertice
        self.update_edges()
    
    def update_edges(self):
        edges = []
        self.weight = 0
        self.num_vertice = len(self.vertice)
        for u in range(self.num_vertice-1):
            for v in range(u+1, self.num_vertice):
                if self.matrix[u][v] > 0:
                    self.weight += self.matrix[u][v]
                    edges.append(dict(vertice=[u,v], weight=self.matrix[u][v]))
        self.edges = sorted(edges, key=lambda k: k['weight'])

    def get_weight(self, u, v):
        return self.matrix[u][v]

    def find_neighbors(self, v):
        # find the neighbors for vertex v
        neighbors = []
        edges = self.matrix[v]
        for i in range(self.num_vertice):
            if edges[i] > 0:
                neighbors.append(i)
        return neighbors

    def check_connectivity(self):
        connected_vertice = [0]
        new_neighbors = [0]
        while True:
            neighbors = []
            for v in new_neighbors:
                neighbors += self.find_neighbors(v)
            # check new neighbors
            new_neighbors = []
            for n in neighbors:
                if n in connected_vertice:
                    continue
                new_neighbors.append(n)
            if len(new_neighbors) > 0:
                connected_vertice += new_neighbors
            else:
                break
        return len(connected_vertice) == self.num_vertice

    def find_minimum_connected_edges(self):
        connected_groups = []
        minimum_connected_edges = []
        for e in self.edges:
            u, v = e['vertice']
            gu = -1
            gv = -1
            for g in range(len(connected_groups)):
                mygroup = connected_groups[g]
                if u in mygroup:
                    gu = g
                if v in mygroup:
                    gv = g
            if gu < 0 and gv < 0:
                # form a new group
                connected_groups.append([u,v])
            elif gu >= 0 and gv < 0:
                connected_groups[gu].append(v)
            elif gu <0 and gv >= 0:
                connected_groups[gv].append(u)
            elif gu == gv: # in the same group
                continue
            else:
                # merge 2 groups
                connected_groups[gu] += connected_groups[gv]
                connected_groups.pop(gv)

            minimum_connected_edges.append(e)
            num_connected = sum([len(x) for x in connected_groups])

            if num_connected == self.num_vertice and len(connected_groups) == 1:
                break
        return minimum_connected_edges

    def build_minimum_connected(self):
        minimum_connected_edges = self.find_minimum_connected_edges()
        new_mat = []
        for i in range(self.num_vertice):
            new_mat.append([0]*self.num_vertice)
        for e in minimum_connected_edges:
            u, v = e['vertice']
            new_mat[u][v] = e['weight']
            new_mat[v][u] = new_mat[u][v]
        self.matrix = new_mat
        self.update_edges()

    def viz(self):
        self.update_edges()
        myplot = """graph network {
            rankdir=LR;
            node [shape = circle];
        """
        myplot += "    {};\n".format(" ".join([str(v) for v in range(self.num_vertice)]))
        for e in self.edges:
            u, v = e["vertice"]
            myplot += '''    {} -- {} [ label = "{}" ];\n'''.format(u, v, e['weight'])
        myplot += "}\n"
        return myplot

def parse_network(fname):
    net = []
    with open(fname) as f:
        for line in f:
            line = line.rstrip()
            row = []
            for w in line.split(','):
                if w == '-':
                    row.append(0)
                else:
                    row.append(int(w))
            net.append(row)
    return net

def main(args):
    # test
    matrix = [
        [0, 16, 12, 21, 0, 0, 0],
        [16, 0, 0, 17, 20, 0, 0],
        [12, 0, 0, 28, 0, 31, 0],
        [21, 17, 28, 0, 18, 19, 23],
        [0, 20, 0, 18, 0, 0, 11],
        [0, 0, 31, 19, 0, 0, 27],
        [0,0,0,23, 11, 27, 0]
    ]
    net = Network(matrix)
    net.build_minimum_connected()
    logger.debug("viz:\n{}".format(net.viz()))
    weight = sum([sum(x) for x in matrix]) // 2
    logger.debug("weight saving: {}".format(weight - net.weight))

    matrix = parse_network("data/p107_network.txt")
    net = Network(matrix)
    net.build_minimum_connected()
    weight = sum([sum(x) for x in matrix]) // 2
    logger.debug("original weight: {}".format(weight))
    logger.debug("viz:\n{}".format(net.viz()))

    answer = weight - net.weight

    logger.info("answer: {}".format(answer))
