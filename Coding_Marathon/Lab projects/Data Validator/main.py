"""
Write a program that performs checking on the entered data, specifically it
should check whether the following types of data are entered correctly:
1.Email
2.Website URL
3.Date
4.Number
5.Credit Card Number
6.Mobile Phone Number
The program asks the user to choose one of the above-mentioned types of data
and then enters the data he/she wants to check. For example the user chooses
an Emailoption and then enterswrong@email .Theprogram should check the
format of the email and should tell the user that it is not a valid email. This
applies to all the types of data.
"""


def email_validation(email_address):
    #allowed_symbols = ("-", "_", ".")
    not_allowed_symbols = (" ", ":", ";", "'", ",")
    #email_address_local = email_address.split("@")[0]
    email_address_domain = email_address.split("@")[1]
    email_address_domain_tail = email_address_domain.split(".")[1]

    is_valid = True

    for i in not_allowed_symbols:
        if i in email_address:
            print("The address is invalid: not allowed symbols in it. Please check.")
            is_valid = False

    if email_address.count("@") != 1:
        print("The address is invalid, @ is entered more than once. Please check.")
        is_valid = False

    elif len(email_address_domain_tail) < 1 or len(email_address_domain_tail) > 4 or email_address_domain.count(".") > 1:
        print("The address is invalid: domain is invalid. Please check.")
        is_valid = False

    return is_valid

def url_validation(url):
    is_valid = False
    url = url.strip()                                    #to remove whitespaces
    if url.startswith("http://"):
        is_valid = True
    return is_valid

def date_validation(date):
    is_valid = True
    day, month, year = (date.split("/"))                 #assuming the format is dd/mm/yyyy
    if day not in range(1, 32):
        is_valid = False
    elif month not in range(1, 13):
        is_valid = False
    elif len(year) > 4:                                 #assuming any year is acceptable
        is_valid = False
    return is_valid



def number_validation(number):
    is_valid = False
    number = number.strip()                                 # to remove whitespaces
    number = number.strip(" ")                              #to remove spaces
    if number.isnumeric():
        is_valid = True
    return is_valid



def card_number_validation(number):
    is_valid = False
    number = number.strip()                                 # to remove whitespaces
    number = number.strip(" ")                              #to remove spaces
    if number.isnumeric() and len(number) == 16:
        is_valid = True
    return is_valid



def mobile_validation(number):
    is_valid = False
    number = number.strip()  # to remove whitespaces
    print(number)
    symbols_to_remove = ["(", ")", "-", " "]  # to remove acceptable symbols
    for item in symbols_to_remove:
        if item in number:
            number.replace(item, "")

    if number.startswith("+374") or number.startswith("00374") and number.isnumeric() and len(number) == 8:
        is_valid = True

    return is_valid




user_input = input("Please enter the type of data: ")

if user_input == "Email":
    value = input("Please enter the data itself: ")
    if email_validation(value):
        print(f"The {user_input} is successfully accepted.")
    else:
        print(f"The {user_input} is not accepted.")

elif user_input == "Website URL":
    value = input("Please enter the data itself: ")
    if url_validation(value):
        print(f"The {user_input} is successfully accepted.")
    else:
        print(f"The {user_input} is not accepted.")

elif user_input == "Date":
    value = input("Please enter the data itself: ")
    if date_validation(value):
        print(f"The {user_input} is successfully accepted.")
    else:
        print(f"The {user_input} is not accepted.")

elif user_input == "Number":
    value = input("Please enter the data itself: ")
    if number_validation(value):
        print(f"The {user_input} is successfully accepted.")
    else:
        print(f"The {user_input} is not accepted.")

elif user_input == "Credit Card Number":
    value = input("Please enter the data itself: ")
    if card_number_validation(value):
        print(f"The {user_input} is successfully accepted.")
    else:
        print(f"The {user_input} is not accepted.")

elif user_input == "Mobile Phone Number":
    value = input("Please enter the data itself: ")
    if mobile_validation(value):
        print(f"The {user_input} is successfully accepted.")
    else:
        print(f"The {user_input} is not accepted.")
