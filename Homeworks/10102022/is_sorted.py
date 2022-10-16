#Write a function called is_sorted that is given a list and returns True if the list is sorted and False otherwise.

def is_sorted_func(lst):
    flag1 = True
    flag2 = True
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            flag1 = False
            break
    for i in range(0, len(lst)):
        if lst[i - 1] < lst[i]:
            flag2 = False
            break
    return (flag1 or flag2)

lst = [1, 2, 3, 4, 5, 3]
print(is_sorted_func(lst))
