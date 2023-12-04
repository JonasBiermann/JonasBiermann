matrix = [
    [1, 2],
    [0, 2],
    [4, 3],
    [4, 2],
    [4, 4]
]

values = {
    'a':0,
    'b':1,
}

def dea(matrix, word, end_states):
    current = 0
    word = list(word)
    while word:
        if word[0] not in values.keys():
            raise Exception('All characters must be in the alphabet of the language!')
        i = values[word.pop(0)]
        current = matrix[current][i]
    if current in end_states:
        return True
    return False

word = input('Was ist ihr Wort?')
print(dea(matrix, word, [2]))