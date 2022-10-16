#Write a function called merge that takes two already sorted lists of possibly different lengths,
#and merges them into a single sorted list. Do this without using the sort method.

def merge_2_lists(lst1, lst2):
    merged_lst = []
    if max(lst1) < min(lst2):
        merged_lst = lst1 + lst2
    elif max(lst2) < min(lst1):
        merged_lst = lst2 + lst1
    else:
        merged_lst = lst1
        for i in lst2:
            for j in merged_lst:
                if i < j and i not in merged_lst:
                    merged_lst.insert(merged_lst.index(j), i)

    return merged_lst

lst1 = [1, 3, 5, 7]
lst2 = [2, 4, 6]

lst3 = [5, 7, 9]
lst4 = [-1, 0, 1]
print(merge_2_lists(lst1, lst2))     #[1, 2, 3, 4, 5, 6, 7]
print(merge_2_lists(lst3, lst4))     #[-1, 0, 1, 5, 7, 9]