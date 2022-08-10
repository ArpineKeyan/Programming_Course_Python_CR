"""
Տրված ֆայլում պարունակվում է տեքստ։ Իրականացնել ծրագիր, որը ֆայլի
մեջ պարունակվող տեքստի բոլոր բառերի առաջին տառերը դարձնում է մեծատառ
և ձևափոխված ամբողջ տեքստը պահպանում մեկ այլ ֆայլում։
"""

with open("Text_to_pr2.txt", "r") as file:
    text = file.readlines()
    with open("Text_to_pr2_titled.txt", "w") as f:
        for item in text:
            f.write(item.title())
            print(item.title())

