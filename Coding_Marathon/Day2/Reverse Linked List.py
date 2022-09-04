"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

head = [1, 2, 3, 4, 5]
if not head:
    print([])
else:
    print(head[::-1])


"""
def reverse_list(lst):
    n_lst = []
    i = len(lst) - 1
    while i >= 0:
        n_lst += [lst[i]]
        i -= 1
    return n_lst

lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))
"""

