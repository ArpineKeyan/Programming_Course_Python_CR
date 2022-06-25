"""
8. Իրականացնել ֆունկցիա, որը վերադարձնում է ամսվա օրերի քանակը։ Ֆունկցիան պետք է ստանա երկու արգումենտ՝
տարեթիվը և ամիսը (ամիսը ստանալ որպես թիվ 1-ից 12 միջակայքում)։ Հաշվի առնել նաև նահանջ տարվա հանգամանքը։
"""


def NumOfDaysInMonth(month, year):
    num_of_days = 30
    if month == 2:
        if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
            num_of_days = 29
        else:
            num_of_days = 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        num_of_days = 31

    return num_of_days


month = int(input("Please enter the month as an integer in range [1, 12]: "))
year = int(input("Please enter the year as a 4 digit integer: "))
print(f"The number of days in {month}/{year} was {NumOfDaysInMonth(month, year)}")
