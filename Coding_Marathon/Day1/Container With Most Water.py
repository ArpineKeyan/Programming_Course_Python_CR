"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
max_container = 0
for i in range(len(height)):

    for j in range(i + 1, len(height)):

        if min(height[i], height[j])*(j - i) > max_container:

            max_container = min(height[i], height[j])*(j - i)

print(max_container)




