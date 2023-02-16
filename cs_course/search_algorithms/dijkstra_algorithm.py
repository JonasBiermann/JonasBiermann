u = float('inf')

matrix = [[0, 2, 3, u, u, u, 7, u], [2, 0, u, 1, u, 5, 4, 1], [3, u, 0, u, 3, u, u, u], [u, 1, u, 0, u, 1, u, u], [
    u, u, 3, u, 0, 1, 1, u], [u, 5, u, 1, 1, 0, u, u], [7, 4, u, u, 1, u, 0, 2], [u, 1, u, u, u, u, 2, 0]]

nodes = [[0, None], [u, None], [u, None], [u, None],
         [u, None], [u, None], [u, None], [u, None]]


def findConnections(node):
    connections = []
    for i in range(len(matrix[node])):
        if matrix[node][i] != float('inf') and matrix[node][i] != 0:
            connections.append(i)
    return connections


def assignWeights(connections, node):
    for element in connections:
        nodes[element][0] = matrix[node][element]
        nodes[element][1] = node

    return nodes


print(assignWeights(findConnections(0), 0))


def dijkstra(start):
    while nodes[5][1] == None:
        node = min(nodes[1:])
        assignWeights(findConnections(node), node)
        print(nodes)


print(nodes)
