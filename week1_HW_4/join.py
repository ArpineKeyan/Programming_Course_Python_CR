#join(data, sep) ֆունկցիան, որը data լիստի անդամները ներառում է տողի մեջ՝ միացնելով դրանք sep տողով,
#ֆունկցիան որպես վերջնարդյունք վերադարձնում է այդ տողը

def join(data, sep):
    """

    :param data: the input list
    :param sep: the separator
    :return: returns list items separated with mentioned separator
    """
    str = ""
    for item in data:
        str += item + sep
    return str

print(join(["hi", "bye", "hey"], " - "))
