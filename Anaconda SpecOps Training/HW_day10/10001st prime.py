"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def is_prime(num):
    is_prime = True
    for item in range(2, num):
        if num % item == 0:
            is_prime = False
            break
    return is_prime


prev_prime = 2
index = 1
while index <= 10001:
    if is_prime(prev_prime):
        prev_prime += 1
        index += 1
    else:
        prev_prime += 1
print(f"The prime number with the index {index - 1} is: {prev_prime - 1}.")

#The prime number with the index 10001 is: 104743.









