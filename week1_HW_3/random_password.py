"""
9. Գրել random_passwd(n) ֆունկցիա, որը պատահականության սկզբունքով կգեներացնի n երկարությամբ գաղտնաբառ։
Գաղտնաբառը պետք է կազմված լինի ASCII աղյուսակի 33-ից 126 միջակայքում ընկած սոմվոլներից։
(Օգտվել ներդրված chr ֆունկցիայից, որը վերադարձնում է թվին համապատասխան սիմվոլը ըստ ASCII աղյուսակի, և random գրադարանից)։
"""
import random


def random_passwd(n):
    """
    :param n: length of password
    :return: generated password of required length
    """
    passwd = ""

    while n != 0:
        ascii_symbol = chr(random.randint(33, 126))
        passwd += ascii_symbol
        n -= 1
    return passwd


passwd_length = int(input("Enter the desired length for password: "))
print(f"Here is the suggested password: {random_passwd(passwd_length)}")