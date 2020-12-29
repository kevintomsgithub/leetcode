def kadane(n):
    local_max = global_max = n[0]
    for i in range(1, len(n)):
        local_max = max(n[i], n[i]+local_max)
        if local_max > global_max: global_max = local_max
    return global_max

a = [1, -1, 3, 4, -1]
print(kadane(a))
            