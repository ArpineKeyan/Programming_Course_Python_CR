"""pop(i=None) - եթե արգումենտ չի փոխանցվել,
այսինքն i-ին վերագրվել է None արժեքը, ջնջում է վերջին անդամը,
հակառակ դեպքում ջնջում է i-րդ ինդեքսում գտնվող անդամը,
և անդամը վերադարձվում է որպես արդյունք
"""

def pop_func(data, i=None):
    """remooves the item with given index or remooves last item if index is not given

    """
    if i is None:
        return data[:-1:]
    else:
        return data[:i:] + data[i::]

data = (7, 5, 6, 8, 14, 22)
print(pop_func(data))
print(pop_func(data, 3))


    
