nm = [int(i) for i in input().split()]
rows = nm[1]
cols = nm[0]
matrix = [input().split() for i in range(rows)]
all_zeros_row_col = []
for x in range(cols):
    matrix[i]



for i in range(rows):
    if matrix[i][0] == '0':
        col = True
    for j in range(1, cols):
        if matrix[i][j]  == '0':
            matrix[0][j] = 0
            matrix[i][0] = 0
for i in range(1, rows):
    for j in range(1, cols):
        if not matrix[i][0] or not matrix[0][j]:
            matrix[i][j] = 0
if matrix[0][0] == 0:
    for j in range(cols):
        matrix[0][j] = 0
if is_col:
    for i in range(Rrows:
    matrix[i][0] = 0
for l in matrix:
    print(' '.join(map(str, l)))