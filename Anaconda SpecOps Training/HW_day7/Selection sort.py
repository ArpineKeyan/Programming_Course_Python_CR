
def selection_sort(lst):

    for i in range(len(lst) - 1):
        _min = i
        for j in range(i + 1, len(lst)-1):
            if lst[j] < lst[_min]:
                _min = j
        lst[i], lst[_min] = lst[_min], lst[i]
    return lst



given_lst = [1, 3, 11, 7, 20, 13]
sorted = selection_sort(given_lst)
print(sorted)
