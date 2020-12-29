def generate_pair(n):
    unique_pairs = []
    for i in range(1, (n+1)//2):
        unique_pairs.append([i, n-i])
    return unique_pairs
    
def generate_more_pairs(p):
    new_pairs = []
    for index, value in enumerate(p):
        if value > 2:
            pair_of_p = generate_pair(value)
            for pair in pair_of_p:
                if pair[0] not in p[:index] and pair[1] not in p[:index]:
                    new_pairs.append(sorted(p[:index] + pair + p[index+1:]))
    return new_pairs

def solution(n):
    queue = generate_pair(n)
    visited = [str(i) for i in queue]
    while queue:
        s = queue.pop(0)
        new_pairs = generate_more_pairs(s)
        for pair in new_pairs:
            if str(pair) not in visited:
                visited.append(str(pair))
                queue.append(pair)
    return len(visited)

import time    

s = time.time()
print(solution(50))
print('Time Taken: ', time.time() - s)