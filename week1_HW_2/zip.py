"""
Գրել zip(data1, data2) ֆունկցիա, որը կվերադարձնի նոր լիստ, հետևյալ տեսքով
[ [data1[0], data2[0]], [data1[1], data2[1]], … [data1[n - 1], data2[n - 1] ],
որտեղ n-ը data1-ի և data2-ի երկարությունն է։
"""


def map_func(data1, data2):
    """

    :param data1: any data
    :param data2: any data
    :return: list with inbuilt zip function's functionality for inputted data
    """
    gen_list = []
    for index in range(len(data1)):
        gen_list.append(data1[index])
        gen_list.append(data2[index])

    return gen_list


data1 = ("Hi", "Hey", "Hello")
data2 = ("Ann", "Mary", "John")
print(map_func(data1, data2))