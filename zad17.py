n = input()
n = int(n)
list = []
for i in range(n):
    dane = input()
    dane = dane.split()
    listA = []
    listA = dane
    list.append(listA)

K = 'Kelvin'
C = 'Celsius'
F = 'Fahrenheit'
for i in range(len(list)):
    a = list[i][0]
    a = float(a)
    if list[i][1] == K and a < 0:
        print('NO')
    elif list[i][1] == C and a < -273.15:
        print('NO')
    elif list[i][1] == F and a < -459.67:
        print('NO')
    elif list[i][1] == K and list[i][2] == K:
        print(f'{(a):.2f}')
    elif list[i][1] == K and list[i][2] == C:
        print(f'{(a-273.15):.2f}')
    elif list[i][1] == C and list[i][2] == K:
        print(f'{(a + 273.15):.2f}')
    elif list[i][1] == K and list[i][2] == F:
        print(f'{(((a - 273.15)*1.8)+32):.2f}')
    elif list[i][1] == F and list[i][2] == K:
        print(f'{(((a-32)/1.8) + 273.15):.2f}')
    elif list[i][1] == F and list[i][2] == F:
        print(f'{(a):.2f}')
    elif list[i][1] == C and list[i][2] == C:
        print(f'{(a):.2f}')
    elif list[i][1] == C and list[i][2] == F:
        print(f'{((a)*1.8 + 32):.2f}')
    elif list[i][1] == F and list[i][2] == C:
        print(f'{((a - 32)/1.8):.2f}')
