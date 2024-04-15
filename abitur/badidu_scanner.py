words = ['dudubabadudubabadudu', 'didudubadududi', 'dudubadibadibadu', 'dididudidibadibadididudidi', 'bo']
terminals = ['ba', 'di', 'du']

def tokenize(word):
    tokens = []
    for i in range(0, len(word), 2):
        tokens.append(word[i:i+2])
    return tokens

def grammar(word):
    global valid
    valid = True
    tokens = tokenize(word)
    
    def checkA(token):
        if ''.join(token) not in ['baba', 'didi', 'dudu']:
            global valid
            valid = False

    def checkS(front_token, end_token):
        # print(front_token, end_token)
        if len(tokens) > 1:
            if front_token in terminals and end_token in terminals and front_token != end_token:
                global valid
                valid = False
            else:
                tokens.pop()
                tokens.pop(0)
                if len(tokens) == 2:
                    checkA(tokens)
                if len(tokens) > 2:
                    checkS(tokens[0], tokens[-1])
                if len(tokens) == 1:
                    if tokens[0] not in ['ba', 'di', 'du']:
                        valid = False
        else:
            if tokens[0] not in ['ba', 'di', 'du']:
                valid = False

    checkS(tokens[0], tokens[-1])
    return valid
    
for word in words:
    print(grammar(word))