"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(num):
    is_prime = True
    for item in range(2, num // 2):
        if num % item == 0:
            is_prime = False
            break
    return is_prime

number = 13195
for factor in range(number, 2, -1):
    if is_prime(factor) and number % factor == 0:
        break
print(factor)

#not sure if this should work this longer for 600851475143

