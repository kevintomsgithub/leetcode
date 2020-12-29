def iterative_levenshtein(s, t):
    """ 
        iterative_levenshtein(s, t) -> ldist
        ldist is the Levenshtein distance between the strings 
        s and t.
        For all i and j, dist[i,j] will contain the Levenshtein 
        distance between the first i characters of s and the 
        first j characters of t
    """

    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    # source prefixes can be transformed into empty strings 
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = i

    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = i
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1,      # deletion
                                 dist[row][col-1] + 1,      # insertion
                                 dist[row-1][col-1] + cost) # substitution

    for r in range(rows):
        print(dist[r])
    
    return dist[row][col]

def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])

    return res


def string_edit_distance(a, b):
    # +1 for the null character reduction
    rows = len(a) + 1
    cols = len(b) + 1
    # Making the memory table
    distance_map = [ [0]*cols for _ in range(rows)]

    # Populating with precalculated values for row-0, col-i
    for i in range(1, rows):
        distance_map[0][i] = i
    # Populating with precalculated values for col-0, row-i
    for i in range(1, cols):
        distance_map[i][0] = i

    # Populating the rest of the values in the table
    for row in range(1, rows):
        for col in range(1, cols):
            if a[row-1] == b[col-1]:
                cost = 0
            else:
                cost = 1
            distance_map[row][col] = min(
                distance_map[row-1][col] + 1,
                distance_map[row][col-1] + 1,
                distance_map[row-1][col-1] + cost,
            )

    for i in range(rows):
        print(distance_map[i])

    return distance_map[row][col]


string_1 = 'kevin'
string_2 = 'tomsn'

x = string_edit_distance(string_1, string_2)
print('--')
x = iterative_levenshtein(string_1, string_2)
print(x)