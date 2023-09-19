number = input("Welche Zahl soll untersucht werden? ")

cond = [[0, 1][2, 1][0, 0]]

def checkNumber(number, curCond):
    dea = []
    for n in number:
        curCond = cond[curCond][int(n)]
    dea.append(curCond)
    