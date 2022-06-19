""" max(data) - վերադարձնում է data-ի ամենամեծ անդամը"""

def max_func_v1(data):
    """returns max of given data

    """
    return max(data)

print(f"The max element of given data is: {max_func_v1([5, 3, 11])}")



def max_func_v2(data):
    """returns max of given data

    """
    index = 0
    max = data[0]
    for item in data:
        if item > max:
            max, item = item, data[index + 1]
    return max

 
print(f"The max element of given data is: {max_func_v2([5, 3, 0])}")   
