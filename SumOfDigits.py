# def digital_root(n):
#     num = str(n)
#     sum = 0
#     for i in num:
#         sum += int(i)
#     if len(str(sum)) == 1:
#         print(sum)
#     else:
#         digital_root(sum)


# digital_root(132189)

def digital_root(n):
    num = 0
    while len(str(n)) > 1:
        for i in str(n):
            num += int(i)
        n = num
        num = 0
    print(n)


digital_root(132189)
