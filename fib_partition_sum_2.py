combinations = []

def helper(arr, sub, i):
    if i == len(arr):
        print(sub)
    else:
        sub[i] = 0
        helper(arr, sub, i+1)
        sub[i] = 1
        helper(arr, sub, i+1)

def find_fib_combinations(n):
    fib = [1, 2]
    for _ in range(1, n):
        next_value = fib[-1] + fib[-2]
        if n < next_value:
            break
        fib.append(next_value)
    print(fib)
    dummy_arra = [0 for i in fib]
    return helper(fib, dummy_arra, 0)

x = find_fib_combinations(15)
print(x)
