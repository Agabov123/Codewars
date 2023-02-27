def solution(s):
    new_string = ""
    for i in s:
        if i.isupper() == True:
            new_string += " "
            new_string += i
        else:
            new_string += i
    return new_string


solution("camelCase")
