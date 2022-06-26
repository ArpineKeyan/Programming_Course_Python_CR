"""
Գլխավոր մրցանակը շահելու համար վիճակախաղի տոմսի վեց համարները պետք է համընկնեն խաղարկության ժամանակ
պատահականության սկզբունքով խաղարկված վեց թվերի հետ՝ 1-ից 49 միջակայքում: Գրեք ծրագիր, որը պատահականորեն
կընտրի ձեր տոմսի համար վեց թիվ: Համոզվեք, որ այդ թվերի մեջ կրկնվող թվեր չկան:
Ցուցադրել տոմսի թվերը էկրանին աճման կարգով:
"""

import random

numbers_list = []

while len(numbers_list) < 6:
    random_number = random.randint(1, 49)
    if random_number not in numbers_list:
        numbers_list.append(random_number)
print(sorted(numbers_list))
