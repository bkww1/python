nm = [int(i) for i in input().split()]
rows = nm[0]
cols = nm[1]
matrix =[]
for n in range(rows):
    matrix.append([int(x) for x in input().split()])
def maxsubmatrix(a,b):
    vecprod = 0
    for i in range(cols):
        for j in range(cols):
            for k in range(cols):
                vecprod += matrix[a+i][b+k]*matrix[a+k][b+j]
    return vecprod

maxsub = 0
for l in range(rows - cols+1):
    for m in range(rows - cols +1):
        sub = maxsubmatrix(l,m)
        if sub > maxsub:
            maxsub = sub

print(maxsub)