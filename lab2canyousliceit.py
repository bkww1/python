list = [int(x) for x in input().split()]
list.sort()
start = list[0]
end = list[-1]

if len(list) == 1:
    wynik = 1
else:
    jump = abs(list[1] - list[0])
    wynik = 0
    new_list = [*range(start, end + 1, jump)]
    if list == new_list:
        wynik = 1


if wynik == 1:
    print('True')
else:
    print('False')