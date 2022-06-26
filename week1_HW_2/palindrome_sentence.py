"""Անգլերեն արտահայտություն
«Is it crazy how saying sentences backwards creates backwards sentences saying how crazy it is?»:
ալինդրոմ նախադասություն է, քանի որ եթե այն կարդաս բառ առ բառ՝ անտեսելով կետադրական նշաններն ու մեծատառերը,
երկու ուղղությամբ էլ նույնը կլինի։ Անգլերեն palindromes բառի օրինակներ են՝
«Herb the sage eats sage, the herb» և
«Information school graduate seeks graduate school information»:
Գրեք ծրագիր, որը կստանա օգտատիրոջից տողը և կտեղեկացնի, եթե դա բանավոր պալինդրոմ է:
Հիշեք, որ արդյունքը հաշվելիս պետք է անտեսել կետադրական նշանները:
"""

user_input = list(input("Please enter your sentence: "))
input_list = []

for item in user_input:
    if item.isalpha():
        input_list.append(str.lower(item))

if input_list == input_list[::-1]:
    print("The input is a palindrome sentence.")

else:
    print("The input is not a palindrome sentence.")