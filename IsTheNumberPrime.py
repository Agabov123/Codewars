def is_prime(num):
    prime = True
    if num < 2:
        prime = False
    elif num == 2:
        prime = True
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

    print(prime)


is_prime(5099)
