def merge(left, right):
    i = j = 0
    sorted_array = []
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i+=1
        else:
            sorted_array.append(right[j])
            j+=1
    sorted_array += left[i:]
    sorted_array += right[j:]
    return sorted_array

def merge_sort(a):
    if len(a) == 1: return a
    mid = len(a)//2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)

def coin_change(coins, amount):
    if amount == 0: return 0
    no_of_coins = 0
    i = len(coins) - 1
    coins.sort()
    while i>=0:
        amount -= coins[i]
        no_of_coins += 1
        if amount == 0:
            return no_of_coins
        elif amount < 0:
            amount += coins[i]
            no_of_coins -= 1
            i -= 1
    return -1

def coin_change_rec(coins, amount):

    if amount == 0: return 0
    dead_amount = amount + 1

    def helper(i, amount, mem={}):
        if amount < 0 or i < 0:  return dead_amount
        if amount == 0: return 0
        if amount in mem: return mem[amount]
        left = helper(i, amount-coins[i], mem) + 1
        right = helper(i-1, amount, mem)
        mem[amount] = min(left, right)
        return mem[amount]
    
    n_coins = helper(len(coins)-1, amount)
    return n_coins if n_coins <= amount else -1

def coin_change_dyn(coins, amount):
    seq = [0] + [amount + 1 for _ in range(amount)]
    for total in range(1, amount+1):
        for coin in coins:
            if coin<=total:
                seq[total] = min(seq[total-coin]+1, seq[total])
    return seq[amount] if seq[amount] <= amount else -1 


def coin_change_rec_uniq(coins, amount):
    def helper(i, amount):
        if amount < 0 or i < 0:  return 0
        if amount == 0: return 1
        left = helper(i, amount-coins[i])
        right = helper(i-1, amount)
        return left + right
    return helper(len(coins)-1, amount)

# coins = [1, 2, 5]
# amount = 4
coins = [3,7,405,436]
amount = 8839

print(coin_change(coins, amount))