def find_max_sum_kadanes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    sum_array = [0 for i in range(rows)]
    local_max = global_max = 0
    for i in range(cols):
        sum_array = [0 for i in range(rows)]
        for k in range(i, cols):
            for j in range(k, rows):
                sum_array[j] += matrix[j][k]
            local_max = max(max(sum_array), sum(sum_array))
            # local_max = max(sum_array)
            if global_max < local_max: global_max = local_max
    return global_max

matrix = [
    [1, 6, 2],
    [0, 6, -1],
    [11, -5, -12],
]
print(find_max_sum_kadanes(matrix))