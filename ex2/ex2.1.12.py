a = int(input('a = '))
b = int(input('b = '))

nod = 2

while (nod % a != 0) or (nod % b != 0):
    nod += 1

print(nod)
