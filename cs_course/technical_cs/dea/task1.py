matrix1 = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 3, 0, 0],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
]

matrix2 = [
    [0, 1],
    [2, 1],
    [0, 0]
]

matrix3 = []

matrix4 = [[1, 4],[1, 2], [3, 4], [3, 2], [4, 4]]

matrix5 = [
    [2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
    [0, 0, 3, 0, 0, 0, 3, 0, 0, 0],
    [3, 0, 0, 0, 3, 0, 0, 0, 3, 0],
    [2, 1, 2, 1, 2, 1, 2, 1, 2, 1]
]

tasks = [matrix1, matrix2, matrix4, matrix5]

def checkInput(curCond, matrix, final):
    number = input('Welche Zahl soll überprüft werden?')
    dea = []
    for n in number:
        curCond = matrix[curCond][int(n)]
        dea.append(curCond)
    
    if curCond == final:
        return True, dea
    return False, dea

finalNodes = [3, 2, 2, 3]

for i in range(0, 5):
    print(checkInput(0, tasks[i], finalNodes[i]))