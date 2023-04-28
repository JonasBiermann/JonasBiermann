key = int(input('what is the key?'))
word = input('whats your word')

alphabet = list(map(chr, range(97, 123)))


def getPointer(_index, _key):
    pointer = _index + _key
    if pointer > 26:
        pointer -= 26
    pointer -= 1
    return pointer


def findChr(_c):
    for value in alphabet:
        if value[0] == _c:
            return value[1]
    return None


def encryptWord(_word, _key):
    encryptedWord = ''
    for i in range(len(alphabet)):
        pointer = getPointer(i, _key)
        alphabet[i] = [alphabet[i], pointer]
    print(alphabet)

    for c in word:
        encryptedWord += alphabet[findChr(c)][0]

    return encryptedWord


for i in range(1, 26):
    print(encryptWord(word, i+1))
