"""
5.  Գրել ծրագիր, որը օգտագործողից ստանում է բառ և արտածում է այդ բառի շրջված տարբերակը (չօգտվել ներդրված մեթոդներից)։
"""

user_input = input("Please enter the word ro reverse: ")
reversed_word = ""
index = len(user_input) - 1

while index >= 0:
    reversed_word += user_input[index]
    index -= 1

print(reversed_word)
