n = int(input())
numbers = [int(x) for x in input().split()]
max_sum = 0
for i in range(n):
    for j in range(i+1,n):
        suba = numbers[i:j+1]
        for k in range(n):
            for l in range(k+1,n):
                subb = numbers(k:l+1)
                if sum(suba[::2]) == sum(subb[::3]) and sum(suba[::2]) > max_sum:
                    max_sum = sum(suba[::2])
print(max_sum)
