num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def create_phone_number(n):
    number = "".join(str(i) for i in n)
    if len(number) == 10:
        final_num = "(" + number[:3] + ")" + \
            " " + number[3:6] + "-" + number[6:10]
        return final_num
    else:
        print("Invalid Input")


def create_phone_number2(n):
    number = "".join(str(i) for i in n)
    if len(number) == 10:
        final_num = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
        return final_num
    else:
        print("Invalid Input")


create_phone_number(num)
