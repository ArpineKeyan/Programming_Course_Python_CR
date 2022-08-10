"""
Հաշվել տրված թվի թվանշանների գումարը։ Օրինակ, տրված է 4637, վերադարձնել 4+6+3+7
"""

given_num = 4637
_sum = 0
while given_num != 0:
    _sum += given_num % 10
    given_num = given_num // 10
print(_sum)