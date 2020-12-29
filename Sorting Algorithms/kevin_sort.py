array = [10, 5, 1, 6, -1, 11, 15, 2]

array_min = min(array)
array_max = max(array)
sorted_array_range = (array_max - array_min) + 1
sorted_array = []

temp_array = ['NaN' for i in range(sorted_array_range)]

for i in array:
    temp_array[array_max-i] = i

for i in temp_array:
    if i != 'NaN':
        sorted_array.append(i)

print(sorted_array)