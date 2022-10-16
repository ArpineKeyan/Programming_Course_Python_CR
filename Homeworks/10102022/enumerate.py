#The enumerate() method adds a counter to an iterable and returns it (the enumerate object).
#The syntax of enumerate() is:  enumerate(iterable, start=0)
#iterable: a sequence, an iterator, or objects that supports iteration
#start (optional): enumerate() starts counting from this number. If start is omitted, 0 is taken as start.

def _enumerate(iterable, start=0):
    """
    The enumerate() method adds a counter to an iterable and returns it (the enumerate object).
    :param iterable: a sequence, an iterator, or objects that supports iteration
    :param start: enumerate() starts counting from this number. If start is omitted, 0 is taken as start
    :return: enumerate() method adds counter to an iterable and returns it. The returned object is an enumerate object.
            In this case it is a list of tuples.
    """
    return_list = []
    for item in iterable:
        return_list.append((start, item))
        start += 1
    return return_list

iter1 = [5, 7, 9, 11, 13]
iter2 = "python"
print(_enumerate(iter1))     #[(0, 5), (1, 7), (2, 9), (3, 11), (4, 13)]
print(_enumerate(iter2, 10)) #[(10, 'p'), (11, 'y'), (12, 't'), (13, 'h'), (14, 'o'), (15, 'n')]
