# The filter() function extracts elements from an iterable (list, tuple etc.) for which a function returns True.
# Its syntax is: filter(function, iterable)
# Parameter	Description
# function:	A Function to be run for each item in the iterable
# iterable:	The iterable to be filtered

def is_positive(num):
    """
    Checks if number is positive or not
    :param num: iterable
    :return: True or False
    """
    if num > 0:
        return True
    else:
        return False


def _filter(func, iter):
    """
    Filters the elements of iterable according to function
    :param func: function to apply on iterable
    :param iter: iterable
    :return: list with iterable elements for which a function returns True
    """
    return_lst = []
    for item in iter:
        if func(item) is True:
            return_lst.append(item)
    return return_lst


my_list = [5, 7, 9, -1, 0, -55]
print(_filter(is_positive, my_list))  # [5, 7, 9]
