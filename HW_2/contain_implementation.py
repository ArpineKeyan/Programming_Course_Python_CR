"""contain(data, val) - ստուգում է, էլեմենտ պարունակվում է լիստում, թե ոչ"""


def contain_v1(data, val):

    """This function checks if the element is in list or not

    """
    return val in data


given_list = [5, 7, "hi", "bye", (5, 7)]
print(f"It is {contain_v1(given_list, 5)} that the given element is in the {given_list}")
print(f"It is {contain_v1(given_list, 3)} that the given element is in the {given_list}")


def contain_v2(data, val):

    """This function checks if the element is in list or not

    """
    index = 0
    is_in_list = False
    for item in data:
        if data[index] != val:
            index += 1
        else:
            is_in_list = True
    return is_in_list
        
print(contain_v2(given_list, "hi"))
print(contain_v2(given_list, "hello"))
