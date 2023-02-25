def dig_pow(n, p):
    num = 0
    for i in str(n):
        num += int(i) ** p
        p += 1
    test = num/n
    if num % n == 0:
        return int(test)
    else:
        print(-1)


dig_pow(92, 1)
