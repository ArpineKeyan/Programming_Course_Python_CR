"""
10. Իրականացնել same_parity(n, *args) ֆունկցիա, որը վերադարձնում է լիստ,
որտեղ գտնվում են ֆունկցիայի այն արգումենտները,
որոնք բաժանվում են n-ի։
"""

def same_parity(n, *args):
    """

    :param n: any int number
    :param args: any number to check division by n
    :return: list with same parity
    """
    same_par = []
    for number in args:
        if number % n == 0:
            same_par.append(number)
    return same_par


print(same_parity(5, 10, 25, 11, 13, 30))