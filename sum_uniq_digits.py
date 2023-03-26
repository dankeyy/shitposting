def sum_uniq_digits(s):
    total = mask = 0

    for n in map(int, s):
        pos = 1 << n
        
        if (mask & pos) == 0:
            total += n
            
        mask |= pos

    return total

 
print(sum_uniq_digits("1122222222334")) # 10
