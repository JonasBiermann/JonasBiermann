key = int(input('what is the key?'))
word = input('whats your word')

alphabet = list(map(chr, range(97, 123)))


def getPointer(index, key):
    pointer = index + key
    if pointer > 26:
        pointer -= 26
    pointer -= 1
    return pointer


def findChr(c):
    for value in alphabet:
        if value[0] == c:
            return value[1]
    return None


def encryptWord(word, key):
    encryptedWord = ''
    for i in range(len(alphabet)):
        pointer = getPointer(i, key)
        alphabet[i] = [alphabet[i], pointer]
    print(alphabet)

    for c in word:
        encryptedWord += alphabet[findChr(c)][0]

    return encryptedWord

def decryptWord(word, key):
    decrypedWord = ''
    for i in range(len(alphabet)):
        pointer = getPointer(i, key)
        alphabet[i] = [alphabet[i], pointer]
    print(alphabet)
    for c in word:
        decrypedWord += alphabet[findChr(c)-key*2][0]

        

print(decryptWord(word, key+1))


