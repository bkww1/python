hwyx = [int(i) for i in input().split()]
h = hwyx[0]
w = hwyx[1]
y = hwyx[2]
x = hwyx[3]
matrix =[]
for i in range(h):
    matrix.append([int(i) for i in input().split()])

def is_there_place(i,j):
    for k in range(y):
        for k in range(x):
            if matrix[i+k][j+l] != 0 or i+k == h or l+j == w:
                return False
    return True
def check_for_place():
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 0:
                if is_there_place(i,j):
                    return True
    return False

if check_for_place():
    print('True')
else:
    print('False')
