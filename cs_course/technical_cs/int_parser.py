def int_parser(scan):
    if not scan:
        return False
    def checkS(i):
        if scan[i][0] == 'op':
            return checkI(i+1)

    def checkI(i):
        check = False
        while i != len(scan):
            if scan[i][0] == 'int':
                i += 1
            else:
                return False
        return True

    if checkS(0):
        return True
    else:
        return False

scan = [['op', '+'], ['int', 1], ['int', 2], ['int', 6]]

print(int_parser(scan))
