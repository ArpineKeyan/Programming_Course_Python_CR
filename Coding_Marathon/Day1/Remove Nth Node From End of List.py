"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

head = [1, 2, 3, 4, 5]
n = 2

new_lst = head[:len(head) - n] + head[(len(head) + 1 - n):]
print(new_lst)
print(head[len(head) - n])
