"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
 and you may not use the same element twice.
You can return the answer in any order.
"""

nums = [2, 7, 11, 15]
target = 9
index_lst = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            index_lst.append(i)
            index_lst.append(j)
print(index_lst)


