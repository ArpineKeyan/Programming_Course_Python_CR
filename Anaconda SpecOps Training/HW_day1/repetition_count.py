"""
Օգտագործելով աղյուսակ (dictionary) հաշվել զանգվածում բոլոր թվերի կրկնությունների քանակը։

"""

given_list = [1, 11, 121, 11, 127, 33, 55, 33, 153, 7, 7, 7, 5, 5, 8, 11, 9]
my_dict = {i: given_list.count(i) for i in given_list}
print(my_dict)

