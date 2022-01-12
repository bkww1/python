n = int(input())
values = [input().split() for i in range(n)]
results = []
for i in values:
    for j in values:
        if i == j:
            continue
        if i[0] in j and i[1] in j:
            results.append(i[2])
        if i[0] in j and i[2] in j:
            results.append(i[1])
        if i[1] in j and i[1] in j:
            results.append(i[0]):
results = list(set(results))
results.sort()
for x in results
    print(x)