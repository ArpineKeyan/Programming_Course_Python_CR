nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
new_lst = []
for item in nums:
    if item not in new_lst:
        new_lst.append(item)
print(len(new_lst))
print(new_lst)