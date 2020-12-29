def reverse_old(x):
    y = []
    x_str = list(str(abs(x)))
    for i in reversed(x_str):
        y.append(i)
    z = int(''.join(y))
    if z > 2**31 - 1:
        return 0
    if x < 0:
        z *= -1
    return z

def reverse_v1(x):
    y = []
    x_str = list(str(abs(x)))
    for i in range(len(x_str)//2):
        j = (len(x_str)-1) - i
        temp = x_str[i]
        x_str[i] = x_str[j]
        x_str[j] = temp
    z = int(''.join(x_str))
    if z > 2**31 - 1:
        return 0
    if x < 0:
        z *= -1
    return z

def reverse1(x):
    y = []
    x_str = list(str(abs(x)))
    mid = len(x_str)//2
    break_flag = 0
    print('Mid : ', mid)
    if len(x_str) % 2 == 0:
        mid_x = mid - 1
        mid_y = mid
    else:
        mid_x = mid - 1
        mid_y = mid + 1
        break_flag += 1
    
    iteration_range = (len(x_str)+1)//4
    
    for i in range(iteration_range):
        # Mid swaps
        print(f'mid_x: {mid_x}, mid_y: {mid_y}')
        temp_mid = x_str[mid_x]
        x_str[mid_x] = x_str[mid_y]
        x_str[mid_y] = temp_mid
        mid_x -= 1
        mid_y += 1
        print(f'After mid swap {i}: {x_str}')
        if break_flag == 1 and i == iteration_range:
            break
        # Extreme swaps
        j = (len(x_str)-1) - i
        temp = x_str[i]
        x_str[i] = x_str[j]
        x_str[j] = temp
        print(f'After out swap {i}: {x_str}')
    z = int(''.join(x_str))
    if z > 2**31 - 1:
        return 0
    if x < 0:
        z *= -1
    return z

print(reverse1(12345678))