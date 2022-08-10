"""
Հաշվել տրված թվի թվանշանների արտադրյալի և գումարի տարբերությունը։ Օրինակ, տրված է 4637, վերադարձնել (4*6*3*7) - (4+6+3+7)
"""

given_num = 4637
_sum = 0
_mul = 1
while given_num != 0:
    _sum += given_num % 10
    _mul *= given_num % 10
    given_num = given_num // 10
print(_mul - _sum)