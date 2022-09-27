"""
Իրականացնում եք`
a program that asks the user to enter a number, checks and prints whether the number is even or odd.
a program that asks the user to enter a character, checks and prints whether the character is a consonant or a vowel.
a program that asks the user to enter n number and prints the n-th Fibonacci number.
a program that asks the user to enter a number and prints the sum of its digits on the screen.
a program that prints the following image on the screen. Use cycles.
*****
*   *
*   *
*   *
*****
"""

#a program that asks the user to enter a number, checks and prints whether the number is even or odd.
user_input = int(input("Please enter a number: "))
if user_input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# a program that asks the user to enter a character, checks and prints whether the character is a consonant or a vowel.
vowels = ('a', 'e', 'i', 'o', 'u')
user_input = input("Please enter a letter: ").lower()
if user_input in vowels:
    print("The letter is vowel.")
else:
    print("The letter is consonant.")


#a program that asks the user to enter n number and prints the n-th Fibonacci number.
fib_prev = 0
fib_next = 1
n = 2
user_input = int(input("Please enter a number n to prints the n-th Fibonacci number: "))
while n <= user_input:
    fib_prev, fib_next = fib_next, fib_prev + fib_next
    n += 1
print(fib_next)


#a program that asks the user to enter a number and prints the sum of its digits on the screen.
user_input = int(input("Please enter a number: "))
digit_sum = 0
while user_input != 0:
    digit_sum += user_input % 10
    user_input = user_input // 10
print(digit_sum)



#a program that prints the following image on the screen. Use cycles.
#    *****
#    *   *
#    *   *
#    *   *
#    *****

matrix = [["*" for i in range(5)] for j in range(5)]
for i in range(1, 4):
    for j in range(1, 4):
        matrix[i][j] = " "
for item in matrix:
    print("".join(item))