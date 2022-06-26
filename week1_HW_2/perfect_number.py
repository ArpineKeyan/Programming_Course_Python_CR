"""
n ամբողջ թիվը կոչվում է կատարյալ, եթե նրա բոլոր բաժանարարների գումարը (բացի իրենից) հավասար է n-ին:
Օրինակ, 28-ը կատարյալ թիվ է, քանի որ դրա բաժանարարներն են 1, 2, 4, 7 և 14, և 1 + 2 + 4 + 7 + 14 = 28:
Գրել ֆունկցիա՝ որոշելու համար, թե արդյոք տվյալ թիվը կատարյալ է: Ֆունկցիան կվերցնի մեկ պարամետր որպես մուտք
և կվերադարձնի True, եթե դա կատարյալ թիվ է, և False՝ հակառակ դեպքում:
"""


def divisor_func(num):
    """

    :param num: user input as an integer
    :return: list of divisors for inputted number
    """

    list_of_divisors = [1]
    for number in range(2, num // 2 + 1):
        if num % number == 0:
            list_of_divisors.append(number)
    return list_of_divisors


user_input = int(input("Please enter a positive number other than 0 or 1: "))
divisors_list = divisor_func(user_input)
print("Divisors list: ", divisors_list)
_sum = 0
for item in divisors_list:
    _sum += item
if _sum == user_input:
    print(f"The number {user_input} is a PERFECT NUMBER.")
else:
    print(f"The number {user_input} is not a PERFECT NUMBER.")

