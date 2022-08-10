# -*- coding: utf-8 -*-
"""HW_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CutGwn9dr3fhrs_-ESZZXf0ebzD7LQ96
"""

#Գրել ծրագիր, որը էկրանին դուրս կբերի Ձեր անունը և հասցեն։
print("Arpine Keyan")

#Գրել ծրագիր, որը օգտատիրոջից ստանում է անունը և էկրանին դուրս բերում ողջույնի հաղորդագրություն օգտագործելով տրված անունը։
user_input = input("Please enter the name: ")
print(f"Hi, {user_input}.")

#Գրել ծրագիր, որը հաշվում է սենյակի մակերեսը։ 
#Այն օգտատիրոջից ստանում է երկարություն և լայնություն ու հաշվում մակերեսը։ 
#Տվյալները փոխանցել float թվերի տեսքով, իսկ վերջնական արդյունքին ավելացնել չափման միավորը։
user_input_length = float(input("Please enter the length: "))
user_input_width = float(input("Please enter the width: "))
print(f"The square area is {user_input_length*user_input_width} square meters")

#Գրել ծրագիր, որը հաշվում է հողամասի մակերեսը։ 
#Այն օգտատիրոջից ստանում է երկարություն և լայնություն ֆունտերով և հաշվում մակերեսը ակռերով։ 
#1 ակռը 43560 ֆունտ քառակուսի է։
user_input_length = int(input("Please enter the length in arcs: "))
user_input_width = int(input("Please enter the width in arcs: "))
measurment = 43560
print(f"The square area is {(user_input_length*user_input_width)*measurment} square meters in pounds.")

#Որոշ երկրներում խրախուսվում է դատարկ ապակե շշերի վերադարձը, և գոյություն ունի հատուկ գնացուցակ։ 
#Օրինակ՝ 1 լիտր և ցածր տարողունակությամբ շշերը արժեն $0.10, իսկ ավելի բարձրերը  $0.25։ 
#Գրել ծրագիր, որը օգտատիրոջից կհարցնի շշերի քանակը յուրաքանչյուր ծավալից և կհաշվի ընդհանուր գումարը։ 
#Արդյունքը պետք է ներկայացնել ստորակետից հետո երկու թվանշանով և ձախից $ նշանով։

one_liter_bottle_price = 0.10
bigger_bottle_price = 0.25

one_liter_bottle_count = int(input("Please eneter the number of one liter bottles: "))
bigger_bottle_count = int(input("Please eneter the number of bigger bottles: "))

one_liter_bottle_total = one_liter_bottle_price * one_liter_bottle_count
bigger_bottle_total = bigger_bottle_price * bigger_bottle_count
print(f"The overall price for the mentioned bottles is: ${one_liter_bottle_total + bigger_bottle_total :.2f}")

#Ծրագիրը որ պետք է գրվի, սկսվում է օգտատիրոջից ռեստորանային պատվերի գումարի հարցումով։ 
#Որից հետո պետք է հաշվարկել հարկերը և թեյավճարը։ Թեյավճարի համար սահմանված է 18%, առանց հարկերը հաշվի առնելու, 
#իսկ հարկերը կազմում են գումարի 20%֊ը։ Ծրագրի աշխատանքի վերջում պետք է դուրս բերվի առանձին հարկերը, 
#թեյավճարը և ամբողջ վճարման ենթակա գումարը։ Թվերը ներկայացնել ստորակետից հետո երկու թվանշանով։

user_input = float(input("Please enter the order amount: "))
additional_cost = round(user_input * 18 / 100, 2)
additional_tax = round(user_input * 20 / 100, 2)
print(f"The additional_cost for this order is: {additional_cost: .2f}")
print(f"The additional tax for this order is: {additional_tax: .2f}")
print(f"The whole amount to pay is: {additional_cost + additional_tax: .2f}")

#Գրել ծրագիր, որը օգտատիրոջից հարցնում է թիվ և հաշվում 1-ից մինչև n ամբողջ թվերի գումարը։
user_input = int(input("Please enter the number: "))
sum = 0
for i in range(user_input):
  sum += i
print(sum)

#Օնլայն խանութը զբաղվում է հուշանվերների և այլ մանրուքների վաճառքով։ Ամեն հուշանվերի քաշը 75 գրամ է, իսկ մանրուքը՝ 112 գրամ։ 
#Գրել ծրագիր, որը օգտատիրոջից հարցնում է գնումների քանակը՝ հուշանվերների և մանրուքների, որից հետո էկրանին դուրս բերել 
#ծանրոցի ընդհանուր քաշը։

souvenir_weight = 75
trifle_weight = 112

souvenir_count = int(input("Please enter souvenirs' count: "))
trifle_count = int(input("Please enter trifles' count: "))

total_weight = souvenir_weight * souvenir_count + trifle_weight * trifle_count
print("The total weight of order is: ", total_weight)

#Պատկերացրեք, որ բանկում բացել եք խնայողական հաշիվ՝ տարեկան 4% տոկոսադրույքով։ 
#Տոկոսները բանկը հաշվում է տարվա վերջում և ավելացնում է հաշվին եղած գումարին։ 
#Գրել ծրագիր, որը օգտատիրոջից հարցնում է նախնական ներդրման չափը, որից հետո հաշվարկում և դուրս է բերում էկրանին առաջին, 
#երկրորդ և երրորդ տարիների հաշվեկշիռը։

yearly_percentage = 4 /100
amount = int(input("Please enter the amount of loan: "))
for i in range(3):
  print(f"Your loan amount for year is {i + 1}: {amount * (1 + yearly_percentage) ** (i+1): .2f}.")

#Գրել ծրագիր, որը օգտատիրոջից հարցնում է a և b ամբողջ թվեր, որից հետո դուրս է բերում էկրանին հետևյալ մաթեմատիկական գործողությունների 
#արդյունքը՝
#  գումարը
#  տարբերությունը
#  բաժանում
#  բաժանման ամբողջ մասը aից b
#  բաժանման մնացորդը aից b
#  տասական լոգարթմը a թվի (օգտագործել math գրադարանը)

import math

a = int(input())
b = int(input())

print(f"The sum: {a + b}")
print(f"The diff: {a - b}")
print(f"The div: {a / b}")
print(f"The div_down: {a // b}")
print(f"The div_rem: {a % b}")
print(f"The lg: {math.log(a, 10)}")

#Ամն֊ում վառելիքի օգտագործումը չափվում են miles-per-gallon(MPG): Միևնույն ժամանակ Կանադայում այս ցուցանիշը չափվում է 
#liters-per-hundred kilometers(L/100km)։ Օգտագործելով Ձեր հետազոտական գիտելիքները, MPG-ն փոխակերպեք L/100km֊ի։ 
#Գրել ծրագիր, որը օգտատիրոջից հարցնում է MPG-ն և դուրս բերում L/100km֊ին։
#1 liter per 100 kilometers equals 235.2 US MPG or 282.5 Imperial MPG
mpg = float(input())
lph = 235.2 * mpg
print(lph)

#Մոլորակի վրա շատ մարդիկ սովոր են մարդու հասակը հաշվարկել ֆուտով և դյույմներով, նույնիսկ եթե նրանց երկիրն ունի մետրային համակարգ: 
#Գրեք ծրագիր, որը հարցնում է օգտատիրոջը, թե քանի ֆուտ և դյույմ է իրենց հասակը: 
#Դրանից հետո պետք է վերահաշվարկի հասակը սանտիմետրերով և ցուցադրի այն էկրանին:                    
#Հուշում. Մեկ ֆուտը հավասար է 12 դյույմ, իսկ մեկ դյույմը հավասար է 2,54 սմ:
ft_input = float(input())
inch_input = float(input())
ft_to_sm = 12 * ft_input * 2.54 + inch_input * 2.54
print(f"{ft_to_sm}sm")

#Այս վարժության համար ձեզ հարկավոր է գրել ծրագիր, որը օգտատիրոջից հարցնում է հեռավորությունը ֆուտով: 
#Դրանից հետո նա պետք է այդ թիվը վերահաշվարկի դյույմերի, յարդերի և մղոնների և դուրս բերի այն էկրանին: 
#Դուք կարող եք հեշտությամբ գտնել միավորների փոխակերպման գործակիցները ինտերնետում։
ft_input = float(input())
inch = ft_input / 12
yard = 36 * inch
mile = 1760 * yard
print("inch - ", inch)
print("yard - ", yard)
print("mile - ", mile)

#Գրեք ծրագիր, որը օգտատիրոջից կհարցնի շառավիղ և կպահպանի այն r փոփոխականում: 
#Դրանից հետո այն պետք է հաշվարկի տվյալ շառավղով շրջանագծի մակերեսը և նույն շառավղով գնդակի ծավալը: 
#Ձեր հաշվարկներում օգտագործեք math մոդուլի pi հաստատունը: Հուշում. Շրջանի մակերեսը հաշվում են area = πr**2 բանաձևով, 
#իսկ գնդի ծավալը՝ volume = 4/3(πr**3)
import math

r = int(input())
area = math.pi * r**2
volume = (4 / 3) * (math.pi * r**3)
print(f"area {area: .2f}")
print(f"volume {volume: .2f}")

#Գլանի ծավալը կարելի է հաշվարկել՝ հիմքում ընկած շրջանագծի մակերեսը բազմապատկելով նրա բարձրությամբ: 
#Գրեք ծրագիր, որտեղ օգտատերը կմուտքագրի գլանի շառավիղը և դրա բարձրությունը, և ի պատասխան կստանա դրա ծավալը՝ 
#կլորացված մինչև մեկ տասնորդական:
import math

r = int(input())
h = int(input())
area = h * math.pi * r**2
print(f"Area is: {area: .2f}")

#Գրեք ծրագիր՝ հաշվարկելու օբյեկտի արագությունը գետնին հասնելու պահին: 
#Օգտատերը պետք է մուտքագրի բարձրությունը մետրերով, որից օբյեկտը բաց է թողնվում: 
#Քանի որ օբյեկտին նախնական արագացում չի տրվել, մենք դրա սկզբնական արագությունը կընդունենք 0 մ/վ: 
#Ենթադրենք, որ ազատ անկման արագացումը 9,8 մ/վ**2: Հաշվի առնելով սկզբնական արագությունը (v), 
#արագացումը (a) և հեռավորությունը (d), կարող եք հաշվարկել արագությունը երբ առարկան դիպչում է գետնին ըստ բանաձևի՝  v**2 + 2ad

d = int(input())
v = 0
a = 9.8
res = v**2 + 2*a*d
print(res)

#Եռանկյան մակերեսը կարելի է հաշվարկել հետևյալ բանաձևով՝                                              
#              area = (b*h)/2                                                                                                       
#որտեղ b-ն եռանկյան հիմքի երկարությունն է, իսկ h-ը՝ բարձրությունը։       
#Գրեք ծրագիր, որը թույլ է տալիս օգտատիրոջը մուտքագրել արժեքներ b և h փոփոխականների համար, 
#որից հետո էկրանին դուրս կբերվի եռանկյունու մակերեսը նշված հիմքով և բարձրությամբ:

b = int(input())
h = int(input())
area = (b*h)/2
print(area)

#Նախորդ վարժությունում մենք հաշվարկել ենք եռանկյան մակերեսը՝ հաշվի առնելով նրա հիմքի երկարությունը և բարձրությունը: 
#Բայց դուք կարող եք նաև հաշվարկել մակերեսը՝ ելնելով եռանկյան բոլոր երեք կողմերի երկարություններից: 
#Դիցուք s1 , s2 և s3 կլինեն կողմերի երկարությունները, և
#              s = (s 1 + s 2 + s 3 )/2:
# Այդ դեպքում եռանկյան մակերեսը կարելի է հաշվարկել հետևյալ բանաձևով.           
#              area = s* (s - s1) * (s- s2) * (s - s3)   
#Գրեք ծրագիր, որը մուտքագրում է եռանկյան բոլոր երեք կողմերի երկարությունները և հաշվարկում է դրա մակերեսը:     
s1 = int(input())
s2 = int(input())
s3 = int(input())
s = (s1 + s2 + s3 )/2
area = s* (s - s1) * (s - s2) * (s - s3)  
print(area)

#Գրել ծրագիր, որը թույլ է տալիս օգտատիրոջը մուտքագրել ժամանակահատված՝ օրերի, ժամերի, րոպեների և վայրկյանների տեսքով և 
#հաշվել վայրկյանների ընդհանուր քանակը տվյալ ժամանակահատվածում:
days = int(input("Please input days: "))
hours = int(input("Please input hours: "))
mins = int(input("Please input minutes: "))
secs = int(input("Please input seconds: "))
day_in_seconds = days * 24 * 60 * 60
hour_in_seconds = hours * 60 * 60
min_in_seconds = mins * 60
total_sec = day_in_seconds + hour_in_seconds + min_in_seconds + secs
print(f"The entered period of {days} days {hours} hours {mins} minutes and {secs} seconds is equal to {total_sec} seconds")

#Python-ի time մոդուլը ներառում է ժամանակի հետ աշխատելու համար շատ օգտակար ֆունկցիաներ: 
#Այս ֆունկցիաներից մեկը՝ asctime-ը, կարդում է համակարգչի ընթացիկ համակարգի ժամանակը և վերադարձնում այն ​​ընթեռնելի տեսքով: 
#Օգտագործեք այս ֆունկցիան՝ ընթացիկ ամսաթիվը և ժամը էկրանին ցուցադրելու համար: Այս անգամ օգտատերից որևէ մուտքի կարիք չեք ունենա:
import time

_time = time.asctime()
print(_time)

#Ամսվա օրերի քանակը տատանվում է 28-ից մինչև 31: 
#Ձեր հաջորդ ծրագիրը պետք է օգտատիրոջից հարցնի ամսվա անունը և ցուցադրի դրա օրերի քանակը:
#Քանի որ մենք տարիները հաշվի չենք առնում, կարող ենք փետրվար ամսվա հաղորդագրություն տպել՝ 
#նշելով, որ այս ամիսը կարող է ունենալ 28 կամ 29 օր՝ նահանջ տարվա գործոնը հաշվի առնելու համար:
months_31 = ("January", "March", "May", "July", "August")
months_30 = ("April", "June", "September")
user_input = input()
if user_input in months_31:
  print(f"{user_input} has 31 day")
elif user_input in months_30:
  print(f"{user_input} has 30 days")
else:
  print("February can have 28 or 29 days.")

#Գրել ծրագիր, որը օգտատիրոջից ստանում է լատինական այբուբենի տառը: 
#Եթե ​​մուտքագրած տառը գտնվում է հետևյալ ցանկում (a, e, i, o կամ u), պետք է տպել հաղորդագրություն, որ տառը ձայնավոր է: 
#Եթե ​​y տառն է մուտքագրվել, ծրագիրը պետք է տպի, որ այս տառը կարող է լինել և ձայնավոր, և բաղաձայն: 
#Մնացած բոլոր դեպքերում պետք է տպվի հաղորդագրություն, որում նշվում է, որ մուտքագրվել է բաղաձայն:
vowels = ("a", "e", "i", "o", "u")
entered_letter = input("Please enter a letter: ")
if entered_letter in vowels:
  print("The letter is vwoel.")
elif entered_letter is "y":
  print("The letter is not vowel nor consonant.")
else:
  print("The letter is consonant.")

#Տարին բաժանված է չորս եղանակների՝ ձմեռ, գարուն, ամառ և աշուն։ 
#Գրել ծրագիր, որը ստանում է օգտատիրոջից օրը և ամիսը՝ սկզբում ամիսը տեքստային ձևով, այնուհետև օրը: 
#Ելքի ժամանակ ծրագիրը պետք է տպի ​​այն սեզոնի անվանումը, որին պատկանում է ընտրված ամսաթիվը:
winter = ("December", "January", "February")
spring = ("March", "April", "May")
summer = ("June", "July", "August") 
autumn =("September", "October", "November")
month = input("Please enter the month: ")
day_input = int(input("Please enter the day: "))
if month in winter:
  print("Winter")
elif month in spring:
  print("Spring")
elif month in autumn:
  print("Autumn")
else:
  print("Summer")

#Գրել ծրագիր՝ օգտատիրոջ մուտքագրած բոլոր թվերի միջինը հաշվարկելու համար: 
#Զրոն կծառայի որպես մուտքագրման ավարտի ցուցիչ: 
#Այս դեպքում ծրագիրը պետք է թողարկի համապատասխան սխալի հաղորդագրություն, 
#եթե օգտագործողի կողմից մուտքագրված առաջին արժեքը զրո է 
#(քանի որ զրոն մուտքագրման ավարտի ցուցանիշն է, այն պետք չէ հաշվի առնել միջինը հաշվարկելիս):
lst = []
user_input = int(input()) 
while user_input != 0:
  lst.append(user_input)
  user_input = int(input()) 
print(sum(lst)/len(lst))

#Գրել ծրագիր՝ ջերմաստիճանների հարաբերակցության աղյուսակը ցուցադրելու համար՝ արտահայտված Ցելսիուսի և Ֆարենհայթի աստիճաններով:
#Աղյուսակում պետք է թվարկվեն 0-ից մինչև 100 աստիճան Ցելսիուսի բոլոր ջերմաստիճանները 10-ի բազմապատիկ:
#To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
i = 0
while i < 101:
  print(f"{i}C is {i * 1.8 +32: .0f}F.")
  i += 10

#Fizz-Buzz-ը հայտնի խաղ է, որն օգնում է երեխաներին խաղային ձևով սովորել բաժանման կանոնները: 
#Մասնակիցները նստում են շրջանաձև, որպեսզի խաղը տեսականորեն շարունակվի անվերջ: 
#Առաջին խաղացողն ասում է «Մեկ» և քայլը փոխանցում ձախ կողմում գտնվողին: 
#Յուրաքանչյուր հաջորդ խաղացող պետք է մտովի ավելացնի մեկը նախորդ թվին և ասի կամ այն, կամ հիմնաբառերից մեկը. 
#Fizz՝ եթե թիվը բաժանվում է երեքի, կամ Buzz՝ եթե այն բաժանվում է հինգի: 
#Եթե ​​այս երկու պայմաններն էլ բավարարվեն, նա ասում է Fizz-Buzz: 
#Այն խաղացողը, ով չի կարողանում ասել ճիշտ բառը, խաղից դուրս է գալիս: 
#Վերջին մնացած խաղացողը ճանաչվում է հաղթող: Մշակեք ծրագիր, որն իրականացնում է Fizz-Buzz խաղի ալգորիթմը առաջին 100 թվերի համար: 
#Յուրաքանչյուր հաջորդ պատասխան պետք է տպվի նոր տողում:

for i in range(1, 101):
  if i % 3 == 0:
    keyword = "Fizz"
  elif i % 5 == 0:
    keyword = "Buzz"
  else:
    keyword = i
  print(keyword)