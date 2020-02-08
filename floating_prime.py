"""
Floating Prime
Author: Woramat Ngamkham
"""
prime_number = []  # Memo for collect prime number to decrease compute time


def floating_prime(num):
    ''' Seperate 1-5 first digit and check is prime  '''
    if (num >= 1 and num <= 10):
        num = int(num * 1000)
        checking_num = [num // 1000, num // 100, num // 10, num]
        for n in checking_num:
            if (is_prime(int(n))):
                return True
    return False


def is_prime(num):
    ''' Check num is a prime number or not '''
    global prime_number
    if (num in prime_number):
        return True
    elif (num > 1):
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i == 0):
                return False
        prime_number.append(num)
        return True
    return False


if __name__ == "__main__":
    next_num = float(input())
    while (next_num != 0):
        if (floating_prime(next_num) == True):
            print("TRUE")
        else:
            print("FALSE")
        next_num = float(input())
