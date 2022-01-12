n = input()
sum = 0

for i in range(0, len(n)):
    for j in range(i, len(n)):
        temp = n[i:j+1]
        if temp[0] == '0':
            continue
        elif temp[-1] =='0':
            for k in range(0, len(temp)):
                if temp[-1-k] != '0':
                    temp = temp[:len(temp)-k]
                    break
        val = True
        for l in range(len(temp)):
            if temp[l] != temp[-1-k]:
                val = False
        if val == True:
            sum += 1
print(sum)