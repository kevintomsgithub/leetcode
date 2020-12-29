def generate_pair(n):
    unique_pairs = []
    for i in range(1, (n+1)//2):
        unique_pairs.append([i, n-i])
    return unique_pairs

def generate_more_pairs(p):
    new_pairs = []
    for index, value in enumerate(p):
        if value > 2:
            pairs_of_p = generate_pair(value)
            for pair in pairs_of_p:
                if pair[0] not in p[:index] and pair[1] not in p[:index]:
                    new_pairs.append(sorted(p[:index] + pair + p[index+1:]))
    return new_pairs

def solution(n):
    generate_pairs = generate_pair(n)
    queue = [i for i in generate_pairs]
    visited = [str(i) for i in queue]
    while queue:
        # print('Queue: ', queue)
        # print('Visited: ', visited)
        s = queue.pop(0)
        new_pairs = generate_more_pairs(s)
        # print('New Pairs: ', new_pairs)
        for pair in new_pairs:
            # print('Pairs: ', pair)
            if str(pair) not in visited:
                visited.append(str(pair))
                queue.append(pair)
    return len(visited)
            
x = [solution(i) for i in range(30)]
for index, i in enumerate(x):
    print(f'N={index} steps = {i}')
