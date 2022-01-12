def count_occurences(sub):
    count = start = 0
    while True:
        start = n.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count
n = n = input()
for i in range(len(n)):
    max_number = n[0:i+1]
    max_occurences = count_occurences(max_number)

    for j in range(len(n)-i):
        number = n[j:j+i+1]
        occurences = count_occurences(number)
        if (occurences > max_occurences) or (occurences == max_occurences and int(number) < int(max_number)):
            max_number = number
            max_occurences = occurences
    print(int(max_number))