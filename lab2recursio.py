import sys
n = input()
n = int(n)
sys.setrecursionlimit(10**6)
rekurencja_memo = {}
def rekurencja(n):
    if n == 1:
        return 1
    elif n not in rekurencja_memo:
        rekurencja_memo[n] = (1 + rekurencja(n - rekurencja(rekurencja(n-1))))
    return rekurencja_memo[n]


print(rekurencja(n))
