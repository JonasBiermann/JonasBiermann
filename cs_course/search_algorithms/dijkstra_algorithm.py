u = float('inf')

matrix = [[0, 2, 3, u, u, u, 7, u], [2, 0, u, 1, u, 5, 4, 1], [3, u, 0, u, 3, u, u, u], [u, 1, u, 0, u, 1, u, u], [
    u, u, 3, u, 0, 1, 1, u], [u, 5, u, 1, 1, 0, u, u], [7, 4, u, u, 1, u, 0, 2], [u, 1, u, u, u, u, 2, 0]]

nodes = [[0, None, False, False], [u, None, False, False], [u, None, False, False], [u, None, False, False],
         [u, None, False, False], [u, None, False, False], [u, None, False, False], [u, None, False, False]]


def findConnections(node):
    nodes[node][2] = True
    connections = []
    for i in range(len(matrix[node])):
        if matrix[node][i] != float('inf') and matrix[node][i] != 0 and nodes[i][3] is not True:
            connections.append(i)
    return connections


def assignWeights(connections, node):
    for element in connections:
        weight = nodes[node][0] + matrix[node][element]
        if weight < nodes[element][0]:
            nodes[element][0] = weight
            nodes[element][1] = node
            nodes[element][2] = True
    nodes[node][2] = False
    nodes[node][3] = True
    return nodes


def currentQueue():
    return [x for x in nodes if x[2] is True and x[3] is not True]


def finished():
    finished = True
    for element in nodes:
        if element[3] == False:
            finished = False
    return finished


def getWeight(node):
    _node = node
    weight = 0
    while nodes[_node][0] != 0:
        weight += nodes[_node][0]
        _node = nodes[_node][1]
    return weight


def dijkstra(finalNode):
    while finished() != True:
        queue = currentQueue()
        if queue != []:
            node = nodes.index(min(queue))
        else:
            node = nodes.index(min(nodes))
        assignWeights(findConnections(node), node)
    path = [finalNode]
    _node = finalNode
    weight = nodes[_node][0]
    while nodes[_node][0] != 0:
        path.append(nodes[_node][1])
        _node = nodes[_node][1]
    return list(reversed(path)), weight


def main():
    for i in range(1, 8):
        finalNode = i
        print(dijkstra(finalNode))


main()
