"""
Գրել ծրագիր, որը օգտատիրոջից սպասում է մուտք՝ բառերի ցանկ, մինչև օգտագործողը թողնի մուտքագրման տողը դատարկ:
Դրանից հետո օգտատիրոջ մուտքագրած բառերը պետք է ցուցադրվեն էկրանին, բայց առանց կրկնությունների՝ յուրաքանչյուրը մեկ անգամ։
Այս դեպքում բառերը պետք է ցուցադրվեն նույն հաջորդականությամբ, որով դրանք մուտքագրվել են ստեղնաշարից:
Օրինակ, եթե օգտվողը ծրագրի խնդրանքով մուտքագրում է բառերի հետևյալ ցանկը.
first
second
first
third
second
ապա ծրագիրը պետք է դուրս բերի․
first
second
third
"""


input_list = []
user_input = input("Please enter first word: ")
while user_input and user_input not in input_list:
    input_list.append(user_input)
    user_input = input("Please enter next word: ")

for item in input_list:
    print(item)