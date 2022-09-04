"""
Given two integer arrays nums1 and nums2,
return an array of their intersection.
Each element in the result must be unique and you may
return the result in any order.
"""

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
intersection = []
if len(nums1) < len(nums2):
    nums1, nums2 = nums2, nums1
for item in nums1:
    if item in nums2 and item not in intersection:
        intersection.append(item)
print(intersection)