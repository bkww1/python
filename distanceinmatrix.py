n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(j) for j in input().split()])
def distance_in_matrix(a, b, c, d):
    if c % a != 0 or d % b != 0:
        return 1000
    return abs(a-c) + abs(b-d)
mdistance = 1000
for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i-1][j-1] == 1:
            for k in range(1, n+1):
                for l in range(1, n+1):
                    if matrix[k-1][l-1] == 1 and (k != i and j != l):
                        distance = distance_in_matrix(i, j, k, l)
                        if distance < mdistance:
                            mdistance = distance
print(mdistance)