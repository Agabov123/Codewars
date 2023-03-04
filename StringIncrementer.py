def increment_string(strng):
    clean = strng.rstrip('1234567890')
    num = strng[len(clean):]
    if num == "":
        strng += "1"
        print(strng)
    else:
        length = len(num)
        print(clean + str(int(num) + 1).zfill(length))


increment_string("f099")
