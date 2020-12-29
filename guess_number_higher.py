def getMoneyAmount(n):
    if n == 1: return 0
    if n == 2: return 1
    if n == 4: return 4
    array = [i for i in range(1, n+1)]
    print(f'array: {array}, len: {len(array)}')
    amount = 0; mid = 0
    while mid < len(array)-2:
        mid = (mid +len(array))//2
        print(f'mid: {mid}, array[mid]: {array[mid]}')
        amount += array[mid]
    return amount

print(getMoneyAmount(4))