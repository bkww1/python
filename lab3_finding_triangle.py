n = input()
n = int(n)
points =[]
for i in range(n):
    point = [float(x) for x in input().split()]
    points.append(point)
areas = []
j = 0
k = 1
for j in range(n-1):
    for k in range(n-1):
        temp_area = ((points[j][0])*(points[k][1])-(points[j][1])*(points[k][0]))
        print(abs(temp_area)/2)
        areas.append(temp_area)
        print(temp_area)
        k += 1
    j +=1
for i in areas:
    if i == 0:
        areas.remove(i)

print(f"{min(areas)} {max(areas)}")