# Write a function called verbose that, given an integer less than 1015, returns the name of the integer in English.
# As an example, verbose(123456) should return one hundred twenty-three thousand, four hundred fifty-six.

def verbose_func(num):
    num_dict = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        30: "thirty",
        50: "fifty"

    }

    if len(list(str(num))) == 4:
        last_two_digits = "".join(list(str(num))[-2:])
        thousand_part = num_dict[int(list(str(num))[0])]
        hundred_part = num_dict[int(list(str(num))[1])]
        decimal_part = ""
        if int(last_two_digits) in num_dict:
            decimal_part += num_dict[int(last_two_digits)]
        elif int(last_two_digits) in range(16, 20):
            decimal_part = decimal_part + "{0}teen".format(num_dict[int(list(str(num))[-1])])
        elif int(last_two_digits) in range(21, 99) and int(last_two_digits[0]) != 3 and int(last_two_digits[0]) != 5:
            decimal_part = decimal_part + num_dict[int(list(str(num))[-2])] + "ty-" + num_dict[int(list(str(num))[-1])]
        elif int(last_two_digits[0]) == 3:
            decimal_part = decimal_part + "thirty-" + num_dict[int(list(str(num))[-1])]
        elif int(last_two_digits[0]) == 5:
            decimal_part = decimal_part + "fifty-" + num_dict[int(list(str(num))[-1])]
        print(f"{thousand_part} thousand {hundred_part} hundred {decimal_part}")


num = int(input("Please enter a 4 digit number of your choice: "))
print("The name of the integer in English is: ")
print(verbose_func(num))
