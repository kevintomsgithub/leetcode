def threeSum(nums):
    result = set()
    mapping = {}
    geq0 = set()
    leq0 = set()
    for i in nums:
        mapping[i] = 1 if i not in mapping.keys() else mapping[i] + 1
        if i >= 0:
            geq0.add(i)
        if i <= 0:
            leq0.add(i)
    for a in geq0:
        for b in leq0:
            c = -a - b
            pair = [a, b, c]
            if c in mapping and mapping[c] >= sum([x==c for x in pair]):
                result.add(tuple(sorted(pair)))
    return result


def three_Sum(nums):
        result = set()
        mapping = {}
        geq0 = set()
        leq0 = set()
        for i in nums:
            mapping[i] = 1 if i not in mapping.keys() else mapping[i] + 1
            if i >= 0:
                geq0.add(i)
            if i <= 0:
                leq0.add(i)
        
        for a in geq0:
            for b in leq0:
                c = - a - b
                potential = [a, b, c]
                if c in mapping.keys() and mapping[c] >= sum([x == c for x in potential]):
                    result.add(tuple(sorted(potential)))
        return result

print(threeSum([-1, 0, 1, 2, -1, -4]))