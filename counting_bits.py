def counting_bits(num):
    if num == 0: return [0]
    if num == 1: return [0, 1]
    seq = [0, 1]
    limit = int(num**(1/2)) + 1
    add_1 = lambda x: x+1
    for _ in range(limit):
        seq += list(map(add_1, seq))
    return seq[:num+1]

def counting_bits_opt(num):
    if num == 0: return [0]
    if num == 1: return [0, 1]
    seq = [0, 1]
    limit = int(num**(1/2)) + 1
    for _ in range(limit):
        next_seq = []
        for i in seq:
            next_seq.append(i+1)
            if len(seq) + len(next_seq) == num+1:
                return seq + next_seq
        seq += next_seq

def counting_bits_opt_sol(num):
    # base case
    if num == 0: return [0]
    # adding first element
    seq = [0]
    # we need to iterate for sqrt(n+1) times
    # n+1 is done to take over the edge case like 8
    limit = int((num+1)**(1/2)) + 1
    for _ in range(limit):
        for i in range(len(seq)):
            # adding 1 to the previous elements
            seq.append(seq[i]+1)
            # return seq if length attained
            if len(seq) == num+1:
                return seq
    return seq

def counting_bits_rec(num):
    
    def helper(limit, num):
        if num == 0: return [0]
        if num == 1: return [0, 1]
        seq = counting_bits_rec(limit-1)
        next_seq = []
        for i in seq:
            next_seq.append(i+1)
            # if len(seq) + len(next_seq) == num+1:
            #     return seq + next_seq
        seq += next_seq
        return seq
    
    limit = int(num**(1/2))
    return helper(limit, num)

def test():
    a = [0, 1, 1, 2]
    for i in range(len(a)):
        a.append(a[i]+1)
    return a

print(counting_bits_opt_sol(8))
# print(test())