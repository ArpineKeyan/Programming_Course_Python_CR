"""
Տրված է անուններ պարունակող ֆայլը
(https://projecteuler.net/project/resources/p022_names.txt),
արտագրել արժեքները մեկ այլ ֆայլում,
որտեղ մեծատառով կլինեն միայն անունների առաջին տառերը։
"""


with open("p022_names.txt", "r") as file:  #opens the given file
    names = file.readlines()               #reads the file in a list line by line
    while names:                           #while there are lines in file
        for item in names:                 #for each item in line 
            titled = item.title()          #makes only first letter uppercase
            with open("p022_names_titled.txt", "w") as f:   #creates new file to write
                f.write(titled)                             #writes in file
            
