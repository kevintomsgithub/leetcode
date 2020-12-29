def maxArea_brute_force(height):
    areas = []
    for i in range(len(height)-1):
        for j in range(i+1, len(height)):
            l = min(height[i], height[j])
            b = j - i
            areas.append(l*b)
    return max(areas)

def maxArea(height):
    if len(height) == 0: return 0
    i = 0
    j = len(height) - 1
    areas = []
    while i!=j:
        l = j - i
        b = min(height[i], height[j])
        areas.append(l*b)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max(areas)


array = [1,8,6,2,5,4,8,3,7]
x = maxArea(array)
print(x)