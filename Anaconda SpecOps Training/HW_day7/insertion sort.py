
def insertion_sort(lst):
    for i in range(1, len(lst)):
        _value = lst[i]

        while lst[i - 1] > _value and i > 0:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i = i - 1
    return lst


given_lst = [4, 6, 8, 3, 2, 5, 7, 9, 0]
print(insertion_sort(given_lst))