nm = [int(i) for i in input().split()]
rows = nm[0]
cols = nm[1]
matrix =[]
for n in range(rows):
    row = input().split()
    for i in row:
        matrix.append(int(i))
matrix.sort()
res = []
for j in range(rows):
    row = []
    for k in range(j,len(matrix),rows):
        row.append(matrix[k])
    res.append(row)
#print(res)
for x in res:
    string = ""
    for y in x:
        string += str(y) + " "
    print(string)

