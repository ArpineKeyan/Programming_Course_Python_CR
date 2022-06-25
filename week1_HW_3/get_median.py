"""
7. Իրականացնել get_median(data) ֆունկցիա, որը վերադարձնում է data լիստի մեդիանը:
"""

def _sort(given_list):
    """
    :param data:
    :return: sorted data
    """
    for i in range(len(given_list)):
        for j in range(len(given_list) - i - 1):
            if given_list[j] > given_list[j + 1]:
                given_list[j], given_list[j + 1] = given_list[j + 1], given_list[j]


    return given_list

def get_median(given_data):
    """
    :param data:
    :return: median of data
    """
    data = _sort(given_data)
    """
    If there is an odd amount of numbers, 
    the median value is the number that is in the middle, 
    with the same amount of numbers below and above
    """
    if len(data) % 2 != 0:
        median = data[len(data)//2]
        """
    If there is an even amount of numbers in the list, 
    the middle pair must be determined, added together, 
    and divided by two to find the median value.
    """
    else:
        median = (data[len(data)//2 - 1] + data[len(data)//2]) / 2

    return median



data = [30, 2, 11, 13, 17, 3, 5, 7, 19, 23]

print(f"The sorted list is: {_sort(data)}")

print(f"And so, the median of {data} is {int(get_median(data))}.")
