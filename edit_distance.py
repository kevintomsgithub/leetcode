'''
  input:  str1 = "dog", str2 = "frog"

  output: 3

  input:  str1 = "some", str2 = "thing"

  output: 9
    '' h o t
  '' 0 1 2 3
  n  1 1 2 3
  o  2 2 1 2
  t  3 2 2 1
  
  str1[i-1] == str2[j-1]:
    dp[i][j] = dp[i - 1][j - 1]
  str1[i-1] != str2[j-1]:
    1 + min()
  

  DD("", "dog")
  '''

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

# print(minDistance('as', ''))
print(minDistance('heat', 'hit'))