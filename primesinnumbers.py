import math
n = input()
l = []
def prime(n):
    if n == 1:
        return False
    for i in range(2,(math.ceil(n/2)+1)):
        if n % i ==0:
            return False
    return True

for j in range(len(n)):
    for k in range(j+1, len(n)+1):
        num = n[j:k]
        if num[0] != '0' and prime(int(num)):
            l.append(num)
l = list(set(l))
l.sort(reverse=True)

for n in list:
    print(n)
