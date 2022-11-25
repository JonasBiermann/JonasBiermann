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
