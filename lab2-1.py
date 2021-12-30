list = []
dane = input()
list = dane.split()
wyniki = []
sum = list[0]
sum = int(sum)
for i in list:
    if int(i) > sum + int(i):
        sum = int(i)
    else:
        sum = sum + int(i)
wyniki.append(sum)
if max(wyniki) < 0:
    print('0')
else:
    print(max(wyniki))
print(wyniki)