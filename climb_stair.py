def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    results = [1, 1]
    for i in range(2, n+1):
        results.append(results[i-1] + results[i-2])
    return results[n]

def climbStairs_btm_up(n, X):
    if n == 0: return 1
    results = {0: 1}
    for i in range(1, n+1):
        total = 0
        for j in X:
            curr_step = i-j
            if curr_step >= 0:
                total += results[curr_step]
        print(f'at {i}: {total}')
        results[i] = total
    return results[n]

steps_allowed = [1, 3, 5]
number_of_steps = 6
print(climbStairs_btm_up(number_of_steps, steps_allowed))