"""
6. Իրականացնել smallest_prime(n) ֆունկցիա, որը վերադարձնում է n-ից մեծ ամենափոքր պարզ թիվը։
"""


def is_prime(num):
    """checks if number is prime or not
    """
    _is_prime = True
    if num == 1 or num == 2:
        _is_prime
    else:
        for item in range(2, num // 2 + 1):
            if num % item == 0:
                _is_prime = False
                break
    return _is_prime


def smallest_prime(the_input):
    """finds the smallest prime number bigger than the input
    """
    i = 1
    while not is_prime(the_input + i):
        i += 1
    return the_input + i


user_input = int(input("Please enter a positive integer number: "))

if user_input == 0:     #handling 0 input
    user_input = int(input("Please enter a positive integer number to continue: "))

print(f"The smallest prime number coming after the {user_input} is: {smallest_prime(user_input)}.")