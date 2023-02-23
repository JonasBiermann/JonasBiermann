matrix = [["x", 3, 4, 2.5], [3, "x", "x", "x"],
          [4, "x", "x", 2], [2.5, "x", 2, "x"]]
knots = ["A", "B", "C", "D"]


def find_weight(start, end):
    return matrix[(knots.index(start))][(knots.index(end))]


print(find_weight("D", "C"))


def nachbarn(knot):
    for i in range(len(matrix[(knots.index(knot))])):
        if matrix[(knots.index(knot))][i] != "x":
            print(knots[i])


print("")
nachbarn("C")
print("")

mini = 10000000


def findshortway(way, end, l):
    global mini
    if way[len(way)-1] != end:
        for i in range(len(matrix[way[len(way)-1]])):
            if matrix[way[len(way)-1]][i] != "x" and i not in way:
                tmp = l+matrix[way[len(way)-1]][i]
                way.append(i)
                findshortway(way, end, tmp)
                way.pop()
    elif way[len(way)-1] == end and l < mini:
        mini = l


findshortway([1], 3, 0)
print(mini)
