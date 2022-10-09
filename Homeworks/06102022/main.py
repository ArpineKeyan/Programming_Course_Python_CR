
#Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
#and asks them how many hours into the future they want to go.
#Print out what the hour will be that many hours into the future, printing am or pm as appropriate.
#An example is shown below.
#Enter hour: 8
#am (1) or pm (2)? 1
#How many hours ahead? 5
#New hour: 1 pm

user_input_hour = int(input("Enter hour: "))
user_input_am_or_pm = int(input("am (1) or pm (2)? "))
user_input_hours_ahead = int(input("How many hours ahead? "))
am_pm = {1: "am", 2: "pm"}

if user_input_hour + user_input_hours_ahead < 12:
    new_hour = user_input_hour + user_input_hours_ahead
    final_am_pm = am_pm[user_input_am_or_pm]

if int(user_input_hour + user_input_hours_ahead) >= 12:
    new_hour = user_input_hour + user_input_hours_ahead - 12
    if user_input_am_or_pm == 1:
        final_am_pm = am_pm[2]
    else:
        final_am_pm = am_pm[1]

print(f"New hour: {new_hour} {final_am_pm}")


#Write a simple quiz game that has a list of ten questions and a list of answers to those questions.
# The game should give the player four randomly selected questions to answer.
# It should ask the questions one-by-one, and tell the player whether they got the question right or wrong.
# At the end it should print out how many out of four they got right.
import random
q_and_a = {
    "Which keyword allows us to load a module in Python?": "import",
    "Which operator can perform floor division in Python?": "/=",
    "Which function can add elements to the end of a list?": "append()",
    "How to declare comments in Python?": "#",
    "A string is immutable in Python?": "True",
    "How do you create a variable with the numeric value 5?": "int(5)",
    "An if statement is written by using the if keyword?": "True",
    "The elif keyword is pythons way of saying if the previous conditions were not true, then try this condition": "True",
    "Tuples are used to store multiple items in a single variable.": "True",
    "Tuples are written with round brackets.": "True"
}
score = 0                                    #score for the right answers
dict_with_q_and_a = {}                       #questions and user answers to show
for i in range(4):                           #selecting 4 random questions
    question = random.choice(list(q_and_a.keys()))
    if question not in dict_with_q_and_a:      #preventing repetition
        print(question)
        user_input = input("Enter your answer: ")
        dict_with_q_and_a[question] = user_input
        if q_and_a[question] == user_input:       #checking if the answer is right
            score += 1                            #increasing the score
print("Your answers: ", dict_with_q_and_a)
print("Your score is: ", score)


# Suppose you have a 5 × 5 list that consists of zeros and M’s.
# Write a program that creates a new 5 × 5 list that has M’s in the same place, but the zeroes are replaced 
# by counts of how many M’s are in adjacent cells (adjacent either horizontally, vertically, or diagonally). 
# An example is shown below. [Hint: short-circuiting may be helpful for avoiding index-out-of-range errors.]
# 0 M 0 M 0     1 M 3 M 1
# 0 0 M 0 0     1 2 M 2 1
# 0 0 0 0 0     2 3 2 1 0
# M M 0 0 0     M M 2 1 1
# 0 0 0 M 0     2 2 2 M 1

matrix_length = 5
given_matrix = [[0, "M", 0, "M", 0], [0, 0, "M", 0, 0], [0, 0, 0, 0, 0], ["M", "M", 0, 0, 0], [0, 0, 0, "M", 0]]
new_matrix = [[0 for i in range(matrix_length)] for j in range(matrix_length)]
minor_matrix = [[]]
for i in range(matrix_length):
    for j in range(matrix_length):
        if given_matrix[i][j] == "M":
            new_matrix[i][j] = "M"
        else:
            if i in range(1, matrix_length - 1) and j in range(1, matrix_length - 1):
                minor_matrix = [[given_matrix[m][n] for m in range(i - 1, i + 2)] for n in range(j - 1, j + 2)]
            if i == 0 and j == 0:
                minor_matrix = [[given_matrix[m][n] for m in range(i, i + 2)] for n in range(j, j + 2)]
            if i == matrix_length - 1 and j == matrix_length - 1:
                minor_matrix = [[given_matrix[m][n] for m in range(i - 1, i + 1)] for n in range(j - 1, j + 1)]
            if i == 0 and j == matrix_length - 1:
                minor_matrix = [[given_matrix[m][n] for m in range(i, i + 1)] for n in range(j - 1, j)]
            if i == matrix_length - 1 and j == 0:     #M[4][0]
                #minor_matrix = [[given_matrix[m][n] for m in range(i - 1, i + 1)] for n in range(j, j + 2)]
                #print("M[4][0]", minor_matrix)
                #a = sum([item.count('M') for item in minor_matrix])
                #calculates right but in final matrix the value prints 1 not 2  - why????????
                #print("a", a)
                #new_matrix[i][j] = sum([item.count('M') for item in minor_matrix])
            if i in (1, matrix_length - 1) and j == 0:
                minor_matrix = [[given_matrix[m][n] for m in range(i - 1, i + 1)] for n in range(j, j + 1)]
            if i == 0 and j in range(1, matrix_length - 1):
                minor_matrix = [[given_matrix[m][n] for m in range(i, i + 1)] for n in range(j - 1, j + 1)]
            if i in (1, matrix_length - 1) and j == matrix_length - 1:
                minor_matrix = [[given_matrix[m][n] for m in range(i - 1, i + 1)] for n in range(j - 1, j)]
            if i == matrix_length - 1 and j in range(1, matrix_length - 1):   #last row
                minor_matrix = [[given_matrix[m][n] for m in range(i - 1, i)] for n in range(j - 1, j + 1)]




            new_matrix[i][j] = sum([item.count('M') for item in minor_matrix])

print(new_matrix)

#should be    [[1, 'M', 3, 'M', 1], [1, 2, 'M', 2, 1], [2, 3, 2, 1, 0], ['M', 'M', 2, 1, 1], [2, 2, 2, 'M', 1]]
#I get this   [[1, 'M', 1, 'M', 1], [0, 2, 'M', 2, 1], [1, 3, 2, 1, 1], ['M', 'M', 2, 1, 1], [1, 2, 1, 'M', 1]]
#6 values are not correct






#Write a program that rotates a matrix by 180 degrees.
#Input:
#1   2   3   4
#5   6   7   8
#9   10  11  12
#13  14  15  16
 
#Output:
#16  15  14  13
#12  11  10  9
#8   7   6   5
#4   3   2   1

matrix_length = 4
given_matrix = [[i + j*2 + 1 for i in range(4)] for j in range(0, 8, 2)]
print(given_matrix)
#output is: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

rotated_matrix = [[0 for i in range(matrix_length)] for j in range(matrix_length)]
for i in range(matrix_length):
    for j in range(matrix_length):
        rotated_matrix[i][j] = given_matrix[matrix_length - i - 1][matrix_length - j - 1]
print(rotated_matrix)
#output is: [[16, 15, 14, 13], [12, 11, 10, 9], [8, 7, 6, 5], [4, 3, 2, 1]]

