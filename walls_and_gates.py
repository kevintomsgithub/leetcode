
def WallsAndGates(room):
    r = len(room)
    c = len(room[0])
    q = []
    visited = set()
    # get all gates
    for i in range(r):
        for j in range(c):
            if room[i][j] == 0:
                visited.add((i, j))
                q.append((i, j))
    steps = 0
    while q:
        for _ in range(len(q)):
            x, y = q.pop(0)
            if room[x][y] == -1: continue
            if room[x][y] == 2**31-1: room[x][y] = steps
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dx, dy = x+dx, y+dy
                next = (dx, dy)
                if 0 <= dx < r and 0 <= dy < c and next not in visited:
                    visited.add(next)
                    q.append(next)
        steps += 1
        
    return room


rooms = [
    [2147483647, -1, 0, 2147483647], 
    [2147483647, 2147483647, 2147483647, -1], 
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]

WallsAndGates(rooms)
print(rooms)