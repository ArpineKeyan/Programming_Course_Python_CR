#* split(source, sep, count) ֆունկցիան, որը source տողը բաժանում է առանձին անդամների ըստ sep տողի,
#և վերադարձնում է լիստ բաղկացած այդ անդամներով

def split(source, sep, count):
    """

    :param source: the string to split by separator
    :param sep: the separator to slpit the string with
    :param count: number of splits
    :return: returns list with splitted parts of string
    """
    j = 0
    lst = []
    for i in range(len(source)):
        if source[i] == sep and count > 0:
            lst.append(source[j:i])
            j = i + 1
            count -= 1
    lst.append(source[j::])
    return lst


string = "Hey there today is a great day!"
sep = " "
count = 3
print(split(string, sep, count))
