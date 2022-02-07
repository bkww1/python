data_list = [int(input()) for i in range(4)]
result_list = []

print(data_list)
for i in range(data_list[3]):
    temp_list = []

    for j in range(data_list[3]):
        temp_list.append(j)
        for k in range(data_list[3]):
            temp_list.append(k)
            result_list.append(temp_list)
print(result_list)