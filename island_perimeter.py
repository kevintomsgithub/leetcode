def islandPerimeter(grid):
    def is_valid_pair(pair):
        i, j = pair
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return False
        return True

    def get_perimeter(m, n):
        boundaries = 0
        pairs = [ [m+1, n], [m-1, n], [m, n+1],[m, n-1] ]
        for pair in pairs:
            i, j = pair
            if is_valid_pair(pair):
                if grid[i][j] == 0: boundaries += 1
            else:
                boundaries += 1
        return boundaries
    
    perimeter = 0
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 1:
    #             perimeter += get_perimeter(i, j)
    # return perimeter
    for i in grid:
        s = ''.join(map(str, i))
        perimeter += sum(2 for k in s.split('0') if k != '')
    for i in zip(*grid):
        s = ''.join(map(str, i))
        perimeter += sum(2 for k in s.split('0') if k != '')
    return perimeter

# grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
grid = [[1, 0]]

print(islandPerimeter(grid))