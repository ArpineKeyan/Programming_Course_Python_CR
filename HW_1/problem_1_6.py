"""
Իրականացնել նախորդ վարժությունում տրված ֆունկցիան՝ հաշվի առնելով,
որ առաջին արգումենտը կարող է մեծ լինել երկրորդից։
Այդ դեպքում ֆունկցիան պետք է վերադարձնի b-ից մինչև a ամբողջ թվերի գումարը։
"""

def num_sum(a, b):
    a = int(a)
    b = int(b)
    res = 0
    while (a <= b):
        res += a
        a += 1
    return res
    


def compared_res(x, y):
    if x < y:
       res = num_sum(x, y)
    else:
        res = num_sum(y, x)
    print(res)

    
        
#print(num_sum(5, 7))
#print(num_sum(3.2, 5.8))
compared_res(7, 5)
