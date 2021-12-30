import numpy as np
matrix_1 = input()
matrix_1_aslist = []
matrix_1_aslist = matrix_1.split()
matryca_pierwsza = []

for i in range(int(matrix_1_aslist[1])):
    matin1_list = []
    matin1 = input().split()
    for j in matin1:
        matin1_list.append(int(j))
    matryca_pierwsza.append(matin1_list)



matrix_2 = input()
matrix_2_aslist = []
matrix_2_aslist = matrix_2.split()
matryca_druga = []

for k in range(int(matrix_2_aslist[1])):
    matin2_list = []
    matin2 = input().split()
    for z in matin2:
        matin2_list.append(int(z))

    matryca_druga.append(matin2_list)

matrix=[[]]
matrix = [[0 for x in range(int(matrix_2_aslist[0]))] for x in range(int(matrix_1_aslist[1]))]

for i in range(len(matryca_pierwsza)):
    for j in range(len(matryca_druga[0])):
        for k in range(len(matryca_druga)):
            matrix[i][j] += matryca_pierwsza[i][k]*matryca_druga[k][j]


for i in range(len(matrix)):
    print(*matrix[i])