"""
Գրեք ֆունկցիա, որը ցույց է տալիս արդյոք իրեն տրված ցանկը որպես պարամետր դասակարգված է (աճման կամ նվազման կարգով):
Ֆունկցիան պետք է վերադարձնի True, եթե ցուցակը դասակարգված է, իսկ հակառակ դեպքում՝ False:
Հիմնական ծրագրում օգտատիրոջից ստացեք թվերի հաջորդականություն ցուցակի համար, այնուհետև տպել հաղորդագրություն՝ ասելով,
թե արդյոք այս ցուցակը ի սկզբանե դասակարգված է:
"""


def is_sorted(data):
    if (sorted(data, reverse=False) == data) or (sorted(data, reverse=True) == data):
        return True
    else:
        return False


input_data_lst = []
_input = input("Please enter your data: ")
while _input:
    input_data_lst.append(int(_input))
    _input = input("Please enter your data: ")

print(f"It is {is_sorted(input_data_lst)} that the input is sorted.")

