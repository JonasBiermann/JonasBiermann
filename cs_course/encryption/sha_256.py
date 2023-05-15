
bytes = []
hexcode = []

def translate(m):
    for c in m:
        byte = bin(ord(c))
        byte = byte[2:]
        if len(byte) < 8:
            byte = '0'* (8-len(byte)) + byte
        
        for bit in byte:
            bytes.append(int(bit)) 
    return bytes

def split(l):
    for i in range(0, len(l), 4):
        yield l[i: i+4]

def convert():
    values = list(split(translate('XO')))
    for v in values:
        hexcode.append(hex(int("".join(map(str, v))))[2:])
        print(hexcode)
        
    return hexcode

print(convert())