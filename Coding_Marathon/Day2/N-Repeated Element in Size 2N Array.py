"""
You are given an integer array nums with the following properties:
nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.
"""

nums = nums = [5, 1, 5, 2, 5, 3, 5, 4]
for item in nums:
    if nums.count(item) > 1:
        print(item)
        break

