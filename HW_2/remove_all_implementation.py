"""
remave_all(data, value) - ջնջում է data-ում եղած բոլոն անդամները, որոնց արժեքը
հավասար է value-ին (իրականացնելիս կարող եք օգտվել remօve մեթոդից)
"""


def remove_all(data, value):
    """removes all identical to given item items from given data

    """
    new_data = []
    for item in data:
        if item != value:
            new_data.append(item)
    
    print(new_data)



remove_all([1, 5, 7, 9, 5, 3, 5, 8], 5)


