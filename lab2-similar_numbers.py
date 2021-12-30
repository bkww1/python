n = input()
n = int(n)
list = []
for i in range(n):
    list.append(int(input()))
informacja = 0
for i in list:
    if list[0] != i:
        informacja = 1
if informacja == 1:
    print('False')
else:
    print('True')