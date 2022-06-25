"""1. Գրել ծրագիր, որն օգտագործողից կստանա թիվ և կտպի այդ թվի շրջված տարբերակը.
        Input: 123
        Output: 321
"""


def num_count(num):                #function to to count digits in given integer number
    given_num = num
    count = 0

    while given_num != 0:
        given_num //= 10
        count += 1

    return count


def reverse_num(num):                 #function to reverse given integer number
    num_length = num_count(num)
    new_num = ""

    while num % 10 == 0:               #handling the case when numbers ends with 0s
        num //= 10
        num_length -= 1

    while num_length != 0:              #main function for reverse
        new_num += str(num % 10)
        num //= 10
        num_length -= 1

    return int(new_num)


user_input = int(input("Please enter the number: "))                     #getting user input
print("The reverse of inputted number {user_input} is: ", reverse_num(user_input))    #function call to check


