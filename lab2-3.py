n = input()
n = int(n)
zbior_prostokatow =  []
for i in range(n):
    zbior_prostokatow.append(int(input()))

stos = []
x = 0
max_powierzchnia = 0
while x < n:
    #stos[-1] -> ostatni element zbioru stos
    if (len(stos) == 0) or (zbior_prostokatow[stos[-1]] <= zbior_prostokatow[x]):
        stos.append(x)
        x += 1
    else:
        gora_stosu = stos.pop()
        if len(stos) > 0:
            powierzchnia = (zbior_prostokatow[gora_stosu] * (x - stos[-1] - 1))
            max_powierzchnia = max(max_powierzchnia, powierzchnia)
        else:
            powierzchnia = zbior_prostokatow[gora_stosu] * x
            max_powierzchnia = max(max_powierzchnia, powierzchnia)

while len(stos) > 0:
    gora_stosu = stos.pop()
    if len(stos) > 0:
        powierzchnia = (zbior_prostokatow[gora_stosu] * (x - stos[-1] - 1))
        max_powierzchnia = max(max_powierzchnia, powierzchnia)
    else:
        powierzchnia = zbior_prostokatow[gora_stosu] * x
        max_powierzchnia = max(max_powierzchnia, powierzchnia)
print(max_powierzchnia)