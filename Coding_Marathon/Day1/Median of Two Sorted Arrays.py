"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""

nums1 = [1, 3]
nums2 = [2]
new_lst = sorted(nums1 + nums2)
if len(new_lst) % 2 == 0:
    median = (new_lst[len(new_lst)//2 - 1] + new_lst[len(new_lst)//2]) / 2
else:
    median = new_lst[len(new_lst)//2]
print(median)