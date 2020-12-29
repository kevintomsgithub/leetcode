def minDistance(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1
    dist_map = [[0]*cols for _ in range(rows)]
    for i in range(cols):
        dist_map[0][i] = i
    for i in range(rows):
        dist_map[i][0] = i
    for row in range(1, rows):
        for col in range(1, cols):
            cost = 0
            if word1[row-1] != word2[col-1]:
                cost = 1
            dist_map[row][col] = min(
                dist_map[row-1][col] + 1,
                dist_map[row][col-1] + 1,
                dist_map[row-1][col-1] + cost,
            )
    return dist_map[rows-1][cols-1]

print(minDistance('as', ''))