nm = [int(i) for i in input().split()]
rows = nm[0]
cols = nm[1]
matrix = [input().split() for i in range(cols)]

for i in range(rows):
    for j in range(cols):
        min_pos = j
        for k in range(j+1, cols):
            if int(matrix[k][i]) < int(matrix[min_pos][i]):
                min_pos = k
        matrix[j][i], matrix[min_pos][i] = matrix[min_pos][i], matrix[j][i]

for l in matrix:
    print(' '.join(map(str, l)))