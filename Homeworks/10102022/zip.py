#The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.
#The syntax of the zip() function is: zip(*iterables)
#iterables:	can be built-in iterables (like: list, string, dict), or user-defined iterables

def _zip(*args):
    """

    :param args: can be built-in iterables (like: list, string, dict), or user-defined iterables
    :return: If we do not pass any parameter, zip() returns an empty iterator
             If a single iterable is passed, zip() returns an iterator of tuples with each tuple having only one element.
             If multiple iterables are passed, zip() returns an iterator of tuples with each tuple having elements from all the iterables.
    """
    return_lst = []
    if len(args) == 0:
        return []
    elif len(args) == 1:    #args = (['x', 'y', 'z'],) in this case
        for item in args[0]:
            return_lst.append((item, ))
    elif len(args) > 1:
        temp_lst = []
        min_length = min([len(item) for item in args])
        for i in range(min_length):
            for item in args:
                temp_lst.append(item[i])
        for i in range(0, len(temp_lst), len(args)):
            return_lst.append(tuple(temp_lst[i: i + len(args)]))

    return return_lst

lst1 = [1, 2, 3]
lst2 = ["x", "y", "z"]
lst3 = ["value", "value", "value", "value"]
print(" No argument: ", _zip())                    #[]
print(" One argument: ", _zip(lst2))                  #[('x',), ('y',), ('z',)]
print(" Two arguments: ", _zip(lst1, lst2))                    #[(1, 'x'), (2, 'y'), (3, 'z')]
print(" Three arguments diff lengths: ", _zip(lst3, lst1, lst2))              #[('value', 1, 'x'), ('value', 2, 'y'), ('value', 3, 'z')]

"""
 No argument:  []
 One argument:  [('x',), ('y',), ('z',)]
 Two arguments:  [(1, 'x'), (2, 'y'), (3, 'z')]
 Three arguments diff lengths:  [('value', 1, 'x'), ('value', 2, 'y'), ('value', 3, 'z')]
"""