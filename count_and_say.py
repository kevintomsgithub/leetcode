def countAndSay(n):
    if n == 1:
        return '1'
    say = '11e'
    for _ in range(n-2):
        new_say = ''
        i=0; j=1
        while i < len(say)-1:
            if say[i] != say[j]:
                reps = str(j-i)
                new_say += reps + say[i]
                i = j
            j += 1
        say = new_say + 'e'
    return say[:-1]

print(countAndSay(1))