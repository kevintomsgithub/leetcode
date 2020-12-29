def generate_fib_numbers(n):
    fib = [1, 2]
    for _ in range(n):
        next_number = fib[-1] + fib[-2]
        if next_number > n:
            break
        fib.append(next_number)
    return fib

def helper(arr, total, subarray, i):
    if total == 0:
        if len(subarray) < len(arr):
            padding = len(arr) - len(subarray)
            [subarray.append(0) for _ in range(padding)]
        binary_fib = ''.join(map(str, subarray))
        solutions.append(binary_fib)
        return 1
    if i < 0:
        return 0
    if total < 0:
        return 0
    if arr[i] > total:
        subarray.append(0)
        helper(arr, total, subarray, i-1)
    else:
        subarray.append(1)
        helper(arr, total-arr[i], subarray, i-1)
        subarray = [0]
        helper(arr, total, subarray, i-1)

def subsum(arr, total, subarray, i):
    if total == 0:
        solutions.append(subarray)
        return 1
    if i < 0:
        return 0
    if total < 0:
        return 0
    if arr[i] > total:
        subsum(arr, total, subarray, i-1)
    else:
        subarray.append(arr[i])
        subsum(arr, total-arr[i], subarray, i-1)
        subarray = []
        subsum(arr, total, subarray, i-1)

def subsum_diff(arr, total, subarray, i, mem):
    key = str([total, i])
    pairs.append(key)
    if key in mem:
        return mem[key]
    if total == 0:
        return 1
    if i < 0:
        return 0
    if total < 0:
        return 0
    if arr[i] > total:
        value = subsum_diff(arr, total, subarray, i-1, mem)
    else:
        subarray.append(arr[i])
        value = subsum_diff(arr, total-arr[i], subarray, i-1, mem)
        if value == 1:
            solutions.append(subarray)
        subarray = []
        value = subsum_diff(arr, total, subarray, i-1, mem)

def fib_base(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_series = generate_fib_numbers(n)
    subsum_diff(fib_series, n, [], len(fib_series)-1, {})


solutions = []
pairs = []
fib_base(10)
print(solutions)