def fib(n, mem):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    if n in mem:
        return mem[n]
    mem[n] = fib(n-1, mem) + fib(n-2, mem)
    return  mem[n]

def get_fib():
    n = 15
    value = [fib(i, {}) for i in range(n)]
    print(f'\n{n} values in sequence: {value}\n')

get_fib()