"""
Գրեք ծրագիր, որը օգտատիրոջից կստանա թվեր, մինչև բաց կթողնվի մուտքագրումը:
Նախ, մուտքագրված թվերի միջին արժեքը պետք է ցուցադրվի էկրանին, որից հետո, մեկը մյուսի հետևից,
անհրաժեշտ է ցուցադրել թվերի ցանկը միջինից ցածր, դրան հավասար (եթե առկա է) և միջինից բարձր:
"""

inputted_numbers = []

user_input = input("Please enter the first number: ")

while user_input:
    inputted_numbers.append(int(user_input))
    print("The List: ", inputted_numbers)

    mean = sum(inputted_numbers)/len(inputted_numbers)
    print("The mean: ", mean)

    for item in inputted_numbers:
        if item < mean:
            print(f"Item {item} is less than mean.")

    for item in inputted_numbers:
        if item == mean:
            print(f"Item {item} is equal to mean.")

    for item in inputted_numbers:
        if item > mean:
            print(f"Item {item} is above mean.")

    user_input = input("Please enter the next number: ")
