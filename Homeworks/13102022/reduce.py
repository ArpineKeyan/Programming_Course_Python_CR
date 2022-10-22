# Implement reduce function (functools) and reduce (itertools)
"""
reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value.
Whereas, accumulate() returns a iterator containing the intermediate results.
The last number of the iterator returned is summation value of the list.
"""


# The reduce(func,seq) function is used to apply a particular function passed in its argument to all of the list elements
# mentioned in the sequence passed along.
# reduce() function works with 3 parameters in python3 as well as for 2 parameters.
# To put it in a simple way reduce() places the 3rd parameter before the value of the second one, if it’s present.
# Thus, it means that if the 2nd argument is an empty sequence, then 3rd argument serves as the default one.
# The syntax is: reduce(function, iterable, initializer=None)


def my_func_power(num, pow):
    return num ** pow

def _reduce(given_func, given_iter, initializer=None):
    if initializer:                                             #case with given initializer
        start = initializer
        for i in range(len(given_iter)):
            num = given_func(start, given_iter[i])
            start = num
    else:
        start = given_iter[0]                                   #case without given initializer - initializer=None
        for i in range(len(given_iter) - 1):
            num = given_func(start, given_iter[i + 1])
            start = num
    return num

lst1 = [2, 3, 2]
val1 = _reduce(my_func_power, lst1, 10)
print("Result of _reduce function with given initializer: ", val1)       #1000000000000
#checking
#a = ((10**2)**3)**2
#print(a)    -> 1000000000000



lst = [5, 2, 2]
val2 = _reduce(my_func_power, lst)
print("Result of _reduce function without the given initializer: ", val2)     #625
#checking
#from functools import reduce
#lst = [5, 2, 2]
#test = reduce(my_func_power, lst)
#print(test)   #625



#accumulate(iter, func):
#It takes two arguments, the first argument is iterable and
# the second is a function which would be followed at each iteration of value in iterable.
# If the function is not defined in accumulate() iterator, addition takes place by default.
# The output iterable depends on the input iterable;
# if input iterable contains no value then the output iterable will also be empty.

def addition_func(num1, num2):
    return num1 + num2

def accumulate_func(given_iter, given_func = addition_func):
    start = given_iter[0]
    lst = [start]
    for i in range(len(given_iter) - 1):
        num = given_func(start, given_iter[i + 1])
        start = num
        lst.append(start)
    return lst


lst3 = [3, 1, 3, 1, 1/3]
val3 = accumulate_func(lst3, my_func_power)
lst4 = [1, 10, 100]
val4 = accumulate_func(lst4)
print("Result of accumulate function with given function:", val3)    #[3, 3, 27, 27, 3.0]
print("Result of accumulate function with given function:", val4)    #[1, 11, 111]

#checking
import itertools
test1 = list(itertools.accumulate(lst3, my_func_power))
print("itertools Test", test1)    # Test [3, 3, 27, 27, 3.0]
