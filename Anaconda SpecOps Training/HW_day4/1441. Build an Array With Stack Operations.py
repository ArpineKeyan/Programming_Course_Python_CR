"""
You are given an array target and an integer n.
In each iteration, you will read a number from list = [1, 2, 3, ..., n].
Build the target array using the following operations:
"Push": Reads a new element from the beginning list, and pushes it in the array.
"Pop": Deletes the last element of the array.
If the target array is already built, stop reading more elements.
Return a list of the operations needed to build target. If there are multiple valid answers, return any of them.

Example 1:
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation:
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

Example 2:
Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]

Example 3:
Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.
"""

target = [1, 3]
n = 3
list = [i + 1 for i in range(n)]            #generating list list = [1, 2, 3, ..., n] for given integer n
output_list = []                            #list for output with "Push", "Pop"
output_list_num = []                        #list to compare with the target to stop when it is already built

for item in list:
    output_list.append("Push")             #adding all items to list one by one
    output_list_num.append(item)
    if item not in target:                 #if item sholdn't be at list, then remooving it
        output_list.append("Pop")
        output_list_num.pop()
    elif output_list_num == target:        #stopping when target is already built
        break


print(output_list)











