def n_queens(n):
    if n<= 0: return None
    q_pos = []

    def is_safe(i, j):
        for x in q_pos[:-1]:
            if x[0]-x[1] == i-j or x[0]+x[1] == i+j or x[0] == i or x[1] == j:
                return False
        return True

    def helper(i, j):
        if i == n: return True
        while j < n:
            q_pos.append([i, j])
            if is_safe(i, j) and helper(i+1, 0):
                return True
            q_pos.pop()
            j +=1
        return False

    can_place = helper(0, 0)
    return can_place, q_pos

n = 6
print(n_queens(n))