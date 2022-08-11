"""
Տեքստային ֆայլի համար իրականացնել ծրագիր, որը կհաշվի ֆայլում հանդիպող սիմվոլների քանակը։
"""

with open("text.txt", "r") as text:                           #opening file to read the text
    lines = text.readlines()                                  #reading all content into list of lists - [[line1], [line2], ..]
    symbol_list = []                                          #empty list
    for item in lines:                                        #collecting list in list items in 1 list bot comfort usage
        for symbol in item:
            symbol_list.append(symbol)
dict = {i: symbol_list.count(i) for i in symbol_list}         #creating dictionary with list items and their count
print(dict)






