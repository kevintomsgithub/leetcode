def getMinimumCost(a, b, m):
    # Sort the items based on their initial cost (a[i])
    items = sorted(zip(a, b), key=lambda x: x[0])
    
    cost = 0
    j = 1

    for i in range(m):
        type_cost = items[i][0] + (j - 1) * items[i][1]
        cost += type_cost
        j += 1

    return cost

# Example usage
n = 2
a = [4, 1]
b = [1, 3]
m = 3

result = getMinimumCost(a, b, m)
print(result)