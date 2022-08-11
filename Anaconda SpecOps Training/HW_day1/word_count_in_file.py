"""
Իրականացնել ծրագիր, որը կհաշվի թե յուրաքանչյուր բառ քանի անգամ է հանդիպում տեքստային ֆայլում
"""

with open("text.txt", "r") as file:
    lines = file.readlines()
    lst = []
    for item in lines:
        for word in item.split(" "):
            if word.isalpha():
                lst.append(word.strip())
dict = {word: lst.count(word) for word in lst}
print(lst)
print(dict)

