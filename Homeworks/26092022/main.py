#Write a program that asks the user for a weight in kilograms and converts it to pounds.
# There are 2.2 pounds in a kilogram.

user_input = int(input("Please enter a weight in kilograms: "))
print("The weight in pounds: ", user_input*2.2)



#Write a program that generates and prints 50 random integers, each between 3 and 6.
import random
random_num_list = []
for i in range(50):
    random_num_list.append(random.randint(3, 6))
print(random_num_list)




#Write a program that asks the user to enter two numbers, x and y , and computes | x − y | /  x+y
x = int(input("Please enter a number: "))
y = int(input("Please enter a number: "))
print(abs(x - y) / (x + y))


# A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also
# divisible by 400. Ask the user to enter a year, and, using the // operator, determine how many leap years there have been
# between 1600 and that year.
param = 1600
user_input = int(input("Please enter a year: "))
if user_input % 4 == 0 or user_input % 100 == 0 and user_input % 400 == 0:
    print("The entered year is Leap year.")
count = (user_input - param) // 4
print(f"Between 1600 and {user_input} there are {count} leap years.") # start and stop are not included



#A number is called a perfect number if it is equal to the sum of all of its divisors, not including the number itself.
#For instance, 6 is a perfect number because the divisors of 6 are 1, 2, 3, 6 and 6 = 1 + 2 + 3.
#As another example, 28 is a perfect number because its divisors are 1, 2, 4, 7,14, 28 and 28=1+2+4+7+14.
#However,15 is not a perfect number because its divisors are 1, 3, 5, 15 and 15 != 1 + 3 + 5.
#Write a program that finds all four of the perfect numbers that are less than 10000.

def divisors(num):
    div_lst = [1]
    for i in range(2, num//2 + 1):
        if num % i == 0:
            div_lst.append(i)
    return(sum(div_lst))

perf_lst = []
for i in range(2, 10000):
    if i == divisors(i):
        perf_lst.append(i)
print(perf_lst)






