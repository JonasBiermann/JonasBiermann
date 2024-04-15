word = input("What's your word? ")

def rightRegular(word):
    global valid
    valid = False
    def checkB(idx):
        if idx < len(word):
            if word[idx] == 'b':
                global valid
                valid = True
        else:
            return False

    def checkA(idx):
        if idx < len(word):
            if word[idx] == 'b':
                checkS(idx + 1)
                checkB(idx + 1)
            return
        else:
            return False

    def checkS(idx):
        if idx < len(word):
            if word[idx] == 'a':
                checkS(idx + 1)
            else:
                if len(word) == 1 and word[idx] == 'b':
                    global valid
                    valid = True
                else:
                    checkA(idx + 1)
            return
        else:
            return False

    checkS(0)
    return valid

print(rightRegular(word))

def leftRegular(word):
    global valid
    valid = False
    
    def checkB(idx):
        if idx == len(word) - 1 and word[idx] == 'a':
            global valid
            valid = True
        else:
            checkB(idx + 1)
        
    def checkA(idx):
        if idx < len(word):
            if word[idx] == 'b':
                checkS(idx + 1)

    def checkS(idx):
        if idx < len(word):
            if word[idx] == 'b' and len(word) == 1:
                global valid
                valid = True
            else:
                checkA(idx + 1)
                checkB(idx + 1)

    checkS(0)
    return valid

print(leftRegular(word[::-1]))