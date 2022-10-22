#Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures.
#That is using closures, one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.

def multiply_with_5(num):
    def nested_func():     #nested function
        return num * 5
    return nested_func  # returns the nested function

multiplier1 = multiply_with_5(3)
print("5 * 3 = ", multiplier1())


def multiplier_func(num1):
    def nested_func(num2):    #nested function
        return num1 * num2
    return nested_func       # returns the nested function

multiplier2 = multiplier_func(4)
value = multiplier2(3)
print("4 * 3 = ", value)



