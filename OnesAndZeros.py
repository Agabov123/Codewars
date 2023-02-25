def binary_array_to_number(arr):
    num = arr[::-1]
    total = 0
    count = 1
    for i in num:
        total += count * i
        count = count * 2
    print(total)


binary_array_to_number([1, 1, 1, 1])
