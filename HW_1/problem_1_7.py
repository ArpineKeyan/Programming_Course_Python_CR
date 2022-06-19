"""
Իրականացնել pow(base, exp) ֆունկցիան՝
հաշվի առնելով, որ exp-ն կարող է լինել նաև ոչ դրական։ Հիշեցնենք
base ** exp = base ** exp, եթե base > 0
base ** exp = (1 / base ** (-exp)), եթե exp < 0
base ** exp = 1, եթե exp = 0
Նաև հաշվի առեք, որ base-ի exp աստիճանը անիմաստ արտահայտություն է,
եթե base-ը հավասար է 0, իսկ exp-ը բացասական է
"""

def my_pow(base, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return base ** exp
    elif exp < 0:
        return 1 / base ** (-exp)

def my_check(base, exp):
    if base == 0 and exp > 0:
        return  f"The {exp}th power of {base} is: 0"
    elif base == 0 and exp < 0:
        return f"The {exp}th power of {base} is undefined."
    else:
        return f"The {exp}th power of {base} is: {my_pow(base, exp)}"
    

    
    
#base = int(input("Please enter the base: "))
#exp = int(input("Please enter the exponent: "))
#print(my_check(base, exp))
print(my_check(1, 0))
print(my_check(1, 2))
print(my_check(2, -1))
print(my_check(0, 5))
print(my_check(0, -5))
 
