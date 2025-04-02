from math import floor, sqrt


def isprime(n):
    if n == 0:
        return False
    elif n == 1:
        return False
    elif n == 2:
        return True
    elif n == 3:
        return True
    else:
        for i in range(2, int(sqrt(n))+1):
            if n % i == 0:
                return False
            else:
                return True
