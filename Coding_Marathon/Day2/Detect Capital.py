"""
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.
"""

word = "Google"
is_upper = True
for item in word:
    if not item.isupper():
        is_upper = False

print(is_upper)



"""
The isupper() method returns True if all the characters are in upper case, otherwise False.
Numbers, symbols and spaces are not checked, only alphabet characters.

def isupper(string):
    is_upper = True
    for i in string:
        if ord(i) in range(97, 123):
            is_upper = False
    return is_upper
"""
