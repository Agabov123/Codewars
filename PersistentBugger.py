def persistence(n):
    itr = 0
    while n > 9:
        itr += 1
        num = str(n)
        total = 1
        for i in num:
            total = total * int(i)
        n = total
    print(itr)


persistence(39)
