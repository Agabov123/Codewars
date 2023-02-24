def maskify(cc):
    newstr = ""
    for i in cc[:-4]:
        newstr += "#"
    newstr = newstr + cc[-4:]
    print(newstr)


maskify("1234567890")
