nm = [int(i) for i in input().split()]
rows = nm[0]
cols = nm[1]
print(nm)

string = input()
matrix = [input() for i in range(rows)]
print(matrix)
i = 0
j = 0
k = 0
curr_row = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == string[k]:
            curr_row = j
            k+=1
            if matrix[i][j+1] in matrix:
                if matrix[i][j+1] == string[k]:



        else:
            j += 1
    else:
        i += 0
        j = 0




      #  for j in range(cols):
        #    if matrix[i][j] == string[k]
