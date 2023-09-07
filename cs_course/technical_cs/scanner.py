def scanner(input):
    input += '#'
    i = 0
    words = {}
    words['la'] = ['pla', 'la']
    words['le'] = ['pla', 'le']
    words['lu'] = ['end', 'lu']

    scan = []
    while input[i] != '#':
        if input[i:i+2] not in words.keys():
            return None
        scan.append(words[input[i:i+2]])
        i += 2

    return scan
