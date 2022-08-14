"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]
"""

nums = [3, 1, 2, 4, 5, 6]
for i in range(len(nums) - 1):                     #starting from first item comparing two neighbour items on being even
    for j in range(i + 1, len(nums)):
        if nums[i] % 2 != 0 and nums[j] % 2 == 0:  #if previous is even and next is odd
            nums[i], nums[j] = nums[j], nums[i]    #we replace them
print(nums)                                        #printing changed list
#[2, 4, 6, 1, 5, 3]


