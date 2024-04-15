matrix = [
    [0, 1],
    [3, 2],
    [3, 1],
    [3, 3],
]

word = input("What is your word? ")
match = {'a':0, 'b':1}
def dea(end_state, matrix, word):
    current_state = 0
    for c in word:
        if c not in match.keys():
            return False
        current_state = matrix[current_state][match[c]]
    
    return current_state == end_state

print(dea(1, matrix, word))