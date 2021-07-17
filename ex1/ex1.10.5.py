A = input('Сколько надо:        ')
B = input('Сколько много:       ')
H = input('Сколько по факту:    ')

A = int(A)
B = int(B)
H = int(H)

if H < A:
    print('Недосып')

if A <= H <= B:
    print('Это нормально')

if H > B:
    print('Пересып')
