"""
Գրել ֆունկցիա, որը ստանում է միջակայքի սկիզբ և վերը (երկու թվեր) և հաշվում միջակայքում գտնվող կենտ թվերի քանակը։
Օրինակ, 3 և 7 միջակայքում կա երեք կենտ թիվ (3, 5, 7)։
"""

range_start, range_stop = int(input("Please enter start: ")), int(input("Please enter stop: "))
count = 0
for item in range(range_start, range_stop + 1):
    if item % 2 != 0:
        count += 1
print(f"The count of even numbers in given range is: {count}.")