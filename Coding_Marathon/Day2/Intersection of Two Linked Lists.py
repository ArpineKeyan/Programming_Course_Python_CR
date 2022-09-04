"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
"""

listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]
intersection = []

for i in range(len(listA)):
    for j in range(len(listB)):
        if listA[i:] == listB[j:]:
            intersection.append(listA[i])
            break
print(intersection[max(len(listA), len(listB)) - min(len(listA), len(listB))])


