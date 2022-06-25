"""
2. Գրեք ծրագիր, որը տրված tuple-ը, որը բաղկացած է ամբողջ թվերից, միացնում է միմյանց որպես թվանշաններ և տպում ստացված արդյունքը.
Example:
tuple: (1, 2, 3)
result: 123
"""


def tuple_to_int(tup):
    number = ""

    for i in range(len(tup)):
        number += str(tup[i])

    return int(number)


given_tuple = (1, 2, 3)
print(tuple_to_int(given_tuple))
