"""
3. Գրել sum_of_min_max(data) ֆունկցիա, որը վերադարձնում է data լիստի ամենամեծ և ամենափոքր թվերի գումարը։
Example:
list: [10,2,5,30]
result: 32
"""


def max_num(data):
    """վերադարձնում է data լիստի ամենամեծ անդամը
    """
    _max = data[0]
    for item in data[1::]:
        if item > _max:
            _max = item
    return _max


def min_num(data):
    """վերադարձնում է data լիստի ամենափոքր անդամը
    """
    _min = data[0]
    for item in data[1::]:
        if item < _min:
            _min = item
    return _min


def sum_of_min_max(data):
    """վերադարձնում է data լիստի ամենամեծ և ամենափոքր թվերի գումարը
    """
    sum_of_min_max = min_num(data) + max_num(data)
    return sum_of_min_max


given_list = [10, 2, 5, 30]
print("The sum of max and min elements in given list is: ", sum_of_min_max(given_list))
