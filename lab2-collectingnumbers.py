n = input()
n = int(n)
list = []
for i in range(n):
    list.append([int(x) for x in input().split()])
sum = [[0 for i in range(n + 1)] for i in range(n + 1)]
print(sum)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum[i][j] = (max(sum[i - 1][j], sum[i][j - 1]) + list[i - 1][j - 1])
        print(sum)
print(sum[n][n])
