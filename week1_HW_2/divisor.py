"""
Գրեք ֆունկցիա, որը կվերադարձնի տվյալ թվի բոլոր բաժանարարների ցանկը:
Այդ թիվը պետք է փոխանցվի ֆունկցիային որպես արգումենտ:
Ֆունկցիայի արդյունքը կլինի թվի բաժանարարների ցուցակը:
"""


def divisor_func(num):
    """

    :param num: user input as an integer
    :return: list of divisors for inputted number
    """

    list_of_divisors = [1]                           #1 is divisor for each number
    for number in range(2, abs(num) // 2 + 1):
        if num % number == 0:
            list_of_divisors.append(number)
    list_of_divisors.append(abs(num))                #number is divisor for itself
    if num > 0:                                      #positive number case
        return list_of_divisors
    elif num < 0:                                    #negative number case
        return [-1 * item for item in list_of_divisors]


user_input = int(input("Please enter a number: "))
if user_input == 0:                                     #0 input case
    print("All numbers are divisors for 0.")
elif user_input == 1:                                   #1 input case
    print(f"Found only one divisor for entered number: {1}")
else:
    print(f"Found following divisors for entered number: {divisor_func(user_input)}")
