"""
Ստեղծել ֆունկցիա, որը ստանում է երկու թվային արգումենտ` a և b,
և վերադարձնում է a-ից մինչև b ընկած ամբողջ թվերի գումարը։
Կարող եք ենթադրել, որ առաջին արգումենտը միշտ փոքր է երկրորդից։
"""
def num_sum(a, b):
    a = int(a)
    b = int(b)
    res = 0
    while (a <= b):
        res += a
        a += 1
    return res 

print(num_sum(5, 7))
print(num_sum(3.2, 5.8))
        
    
    
