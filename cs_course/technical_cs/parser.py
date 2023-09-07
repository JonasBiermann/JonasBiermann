from scanner import *

def parser(scan):
    
    def checkS(i):
        if scan[i][0] == 'pla' or scan[i][0] == 'end':
            return checkA(i+1)
        else:
            return False
    
    def checkA(i):
        if scan[i][0] == 'pla' or scan[i][0] == 'end':
            return checkB(i+1)
        else:
            return False
    
    def checkB(i):
        if scan[i][0] == 'end' and i == len(scan)-1:
            return True
        else:
            return False
    
    if checkS(0):
        return True
    else:
        return False

test = input('What string do you want to check? ')

print(parser(scanner(test)))