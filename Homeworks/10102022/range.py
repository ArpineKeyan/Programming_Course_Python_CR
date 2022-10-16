#The range() function is a built-in-function used in python, it is used to generate a sequence of numbers.

#Start: Optional — An integer number that specifies where to start     (Default value is 0)
#Stop: Required — An integer number that specifies where to stop.
#Step: Optional — An integer number that specifies how much to increment the number (Default value is 1)

def _range(*args):
    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif args[0] != None and args[1] != None and args[2] != None:
        start = args[0]
        stop = args[1]
        step = args[2]

    value = start
    seq = [value]
    if step > 0:
        while value < stop - step:
            value += step
            seq.append(value)
    else:
        while value > stop - step:
            value += step
            seq.append(value)
    return seq

print(_range(1, 5, 2))   #[1, 3]
print(_range(3, 5))      #[3, 4]
print(_range(5))         #[0, 1, 2, 3, 4]
print(_range(1, 5, -2))  #[1]

