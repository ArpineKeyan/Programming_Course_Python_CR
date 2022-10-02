#Write a program that allows the user to enter five numbers (read as strings).
#Create a string that consists of the user’s numbers separated by plus signs.
#For instance, if the user enters 2, 5, 11, 33, and 55, then the string should be ‘2+5+11+33+55’
str = ""                            #empty string
for i in range(5):                  #loop to get numbers as input
    user_input = input("Please enter a number: ")
    str += user_input + " + "
print(str[:-2])                    #printing string without last + sign

#----------------------------------------------------------------------------------------------------------------------


#Write a program that gets a string from the user containing a potential telephone number.
#The program should print Valid if it decides the phone number is a real phone number, and Invalid otherwise.
#A phone number is considered valid as long as it is written in the form abc-def-hijk or 1-abc-def-hijk.
#The dashes must be included, the phone number should contain only numbers and dashes, and the number of digits
#in each group must be correct. Test your program with the output shown below.
#Enter a phone number: 1-301-447-5820 Valid
#Enter a phone number: 301-447-5820 Valid
#Enter a phone number: 301-4477-5820 Invalid
#Enter a phone number: 3X1-447-5820 Invalid
#Enter a phone number: 3014475820 Invalid
user_input = input("Please enter a phone number: ")
flag = "Invalid"
if len(user_input) == 12:
    if user_input[3] == user_input[7] == "-" and user_input.replace("-", "").isnumeric():
        flag = "Valid"
elif len(user_input) == 14:
    if user_input[1] == user_input[5] == user_input[9] == "-" and user_input.replace("-", "").isnumeric():
        flag = "Valid"
print(flag)

#----------------------------------------------------------------------------------------------------------------------


#Use a list comprehension to produce a list that consists of all palindromic numbers between 100 and 1000.
produced_list = [item for item in range(100, 1001) if item == int(str(item)[::-1])]
print(produced_list)

#----------------------------------------------------------------------------------------------------------------------

# Let L=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47].
# Use a list comprehension to produce a list of the gaps between consecutive entries in L.
# Then find the maximum gap size and the percentage of gaps that have size 2.
L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
L_gaps = [L[i + 1] - L[i] for i in range(0, len(L) - 1)]
max_gap = max(L_gaps)
print("Gaps between items: ", L_gaps)
print("Max gap: ", max_gap)
percentage_of_gaps_size_2 = 100 * L_gaps.count(2) / len(L_gaps)
print("% of gaps that have size 2: ", round(percentage_of_gaps_size_2, 2))

#----------------------------------------------------------------------------------------------------------------------

#Write a program that repeatedly asks the user to enter product names and prices.
#Store all of these in a dictionary whose keys are the product names and whose values are the prices.
#When the user is done entering products and prices, allow them to repeatedly enter a product name and
#print the corresponding price or a message if the product is not in the dictionary.
_dict = {}
for i in range(5):
    user_input = input("Please enter product name and price: ")
    key = user_input.split()[0]
    value = user_input.split()[1]
    _dict[key] = value
print(_dict)
for i in range(3):
    product_name = input("Please enter product name and I'll show the price: ")
    if product_name in _dict:
        print(_dict[product_name])
    else:
        print("Product is not there: ")
### Checked for this case:   {'b1': '100', 'b2': '200', 'b3': '300', 'b4': '400', 'b5': '500'}


#----------------------------------------------------------------------------------------------------------------------

#Dictionaries provide a convenient way to store structured data.
# Here is an example dictionary:
#di = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
#      {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
#      {'name':'Princess', 'phone':'555-3141', 'email':''},
#      {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
#Write a program that reads through any dictionary like this and prints the following:
#(a) All the users whose phone number ends in an 8
#(b) All the users that don’t have an email address listed
di = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
      {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
      {'name':'Princess', 'phone':'555-3141', 'email':''},
      {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

for item in di:
    if item['email'] == '':
        print(f"User {item['name']} doesn’t have an email address.")
for item in di:
    if item['phone'][-1] == "8":
        print(f"User {item['name']}'s phone number ends with 8.")

#----------------------------------------------------------------------------------------------------------------------


# Create a 5 × 5 list of numbers.
# Then write a program that creates a dictionary whose keys are the numbers and
# whose values are the how many times the number occurs.
# Then print the three most common numbers.
import random
matrix = [[random.randint(1, 13) for i in range(5)] for j in range(5)]
print("The matrix is: ", matrix)
dictionary = {}
for i in range(5):
    for j in range(5):
        if matrix[i][j] in dictionary.keys():
            dictionary[matrix[i][j]] += 1
        else:
            dictionary[matrix[i][j]] = 1
print("The dict is: ", dictionary)

sorted_values = sorted([value for value in dict.values(dictionary)], reverse=True)
print("Sorted values: ", sorted_values)
d = {k: v for k, v in dictionary.items() if v in sorted_values[:3]}
print("Most common numbers: ", d)

#output1 - but it can vary depending on how many most common keys are there in dict
#The matrix is:  [[10, 6, 4, 5, 11], [13, 6, 6, 6, 12], [11, 1, 7, 12, 12], [1, 7, 7, 6, 4], [2, 6, 7, 2, 7]]
#The dict is:  {10: 1, 6: 6, 4: 2, 5: 1, 11: 2, 13: 1, 12: 3, 1: 2, 7: 5, 2: 2}
#Sorted values:  [6, 5, 3, 2, 2, 2, 2, 1, 1, 1]
#Most common numbers:  {6: 6, 12: 3, 7: 5}

#output2
#The matrix is:  [[9, 11, 2, 11, 5], [2, 4, 3, 3, 2], [2, 2, 5, 11, 6], [1, 7, 7, 9, 10], [9, 7, 11, 1, 3]]
#The dict is:  {9: 3, 11: 4, 2: 5, 5: 2, 4: 1, 3: 3, 6: 1, 1: 2, 7: 3, 10: 1}
#Sorted values:  [5, 4, 3, 3, 3, 2, 2, 1, 1, 1]
#Most common numbers:  {9: 3, 11: 4, 2: 5, 3: 3, 7: 3}
