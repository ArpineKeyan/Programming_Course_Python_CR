"""
Գրել ծրագիր,որը հաշվում է 1-ից 100 թվերի գումարի քառակուսին (1+...+100)^2,
հաշվում է 1-ից 100 թվերի քառակուսիների գումարը՝ (1^2 + 2^2 + … + 100^2)։
Ծրագիրը տպում է ստացված թվերի տարբերությունը։
"""

square_of_sum = sum(range(100))**2
sum_of_squuares = sum([i**2 for i in range(100)])
print(abs(square_of_sum - sum_of_squuares))

#24174150
