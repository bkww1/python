n = input()
n = int(n)
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])
max_sum_in_matrix = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                temp_sum = 0
                for x in range(i,k+1):
                    for y in range(j, l+1):
                        temp_sum = temp_sum + matrix[x][y]
                    if temp_sum > max_sum_in_matrix:
                        max_sum_in_matrix = temp_sum

if max_sum_in_matrix < 0:
    print('0')
else:
    print(max_sum_in_matrix)
    #https://www.interviewbit.com/blog/maximum-sum-rectangle/