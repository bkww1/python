nm = [int(i) for i in input().split()]
rows = nm[0]
cols = nm[1]
matrix = [input().split() for i in range(rows)]
i = 0
pos_r = []
pos_c = []
all_zeros_row = []
for z in range(cols):
    all_zeros_row.append(0)
matrix_copy = matrix
for i in range(cols):
    j = 0
    for j in range(rows):
        if matrix[i][j] == '0':
            matrix[i] = all_zeros_row
            for a in range(rows):
                matrix[a][j] = 0
            j += 1
        else:
            j += 1
for l in matrix:
    print(' '.join(map(str, l)))


r, c = set(), set()
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            r.add(i)
            c.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
for i in range(rows):
        for j in range(cols):
            if i in r or j in c:
                matrix[i][j] = 0
