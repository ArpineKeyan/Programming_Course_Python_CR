#The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns an iterator.
#Its syntax is: map(function, iterable, ...)
#function: a function that perform some action to each element of an iterable
#iterable: an iterable like sets, lists, tuples, etc
#You can pass more than one iterable to the map() function.

def _square(num):
    return num ** 2

def _zip1(func, iter):
    lst = []
    for item in iter:
        lst.append(func(item))
    return lst

def _sum_iter(*args):
    temp_lst = []
    return_lst = []
    min_length = min([len(item) for item in args])
    for i in range(min_length):
        for item in args:
            temp_lst.append(item[i])
    #print(temp_lst)
    for i in range(0, len(temp_lst), len(args)):
        return_lst.append(temp_lst[i] + temp_lst[i + 1])
    return return_lst


def _zip2(func, *args):
    return func(*args)



print(_zip1(_square, [1, 3]))    #[1, 9]
print(_zip2(_sum_iter, [1, 3, 5], [1, 5, 3]))   #[2, 8, 8]

