"""min(data) - վերադարձնում է data-ի ամենափոքր անդամը"""

def min_func_v1(data):
    """returns max of given data

    """
    return min(data)

print(f"The min element of given data is: {min_func_v1([5, 3, 11])}")



def min_func_v2(data):
    """returns max of given data

    """
    index = 0
    min = data[0]
    for item in data:
        if item < min:
            min, item = item, data[index + 1]
    return min

print(f"The min element of given data is: {min_func_v2([5, 3, 0])}")

