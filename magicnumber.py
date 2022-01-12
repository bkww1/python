n = input()
len_n = len(n)


def check_magic(num):
    adv = True
    for i in range(1, len(num)):
        temp_num = num[i - 1]
        if num[i] < temp_num and adv:
            adv = False
        if not adv and num[i] > temp_num:
            return False
    return True


magic = []
for j in range(len_n):
    for k in range(j + 1, len_n + 1):
        if check_magic(n[j:k]):
            magic.append(n[j:k])
magic = list(set([int(x) for x in magic]))
magic.sort()
for y in magic:
    print(y)