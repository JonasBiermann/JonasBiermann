key = int(input('what is the key?'))
word = input('whats your word')

# alphabet = list(map(chr, range(97, 123)))


# def getPointer(index, key):
#     pointer = index + key
#     if pointer > 26:
#         pointer -= 26

#     return pointer


# for i in range(len(alphabet)):
#     p = getPointer(i, key)
#     alphabet[i] = [alphabet[i], p]


for i in range(len(word)):
    value = ord(word[i]) + key
    # word[i] = chr(value)


print(word)
