"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

given_integer = int(input("Please enter a number: "))

if given_integer == int(str(given_integer)[::-1]):
    print("true")
    
else:
    print("false")
                    
