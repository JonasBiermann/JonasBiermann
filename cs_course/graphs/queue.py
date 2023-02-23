import random
# Aufgabe 1
queue = [10, 4, 6, 8, 1, 3, 2]
stack = queue[::-1]
print(queue)
print(stack)

# Aufgabe 2
money = []
type = [0.1, 0.2, 0.5, 1, 2]
for i in range(20):
    money.append(random.choice(type))
print(money)
money.sort()

print(money)

# dishes
t = [0, 1, 1, 1]
b = [1, 0, 1, 1]

if t[::-1] == b:
    print('all good')

# stack and queue for trains
l1 = [5, 4, 3, 2, 1]
l2 = [5, 3, 1, 2, 4]
l3 = [4, 2, 5, 3, 1]
l4 = [1, 4, 5, 3, 2]


def stackMethod(list):
    l1 = list
    l0 = [1, 2, 3, 4, 5]
    l2 = []
    stackList = []
    for i in range(len(list)):
        if l0[i] == l1[i]:
            l2.append(l0[i])
        else:
            stackList.append(l1[i])
        if (stackList != [] and stackList[0] == l1[i+1]):
            l2.append(stackList[0])
            stackList = []
        print('l2', l2)
    if l2 == l1:
        return True
    else:
        return False


print(stackMethod(l3))
