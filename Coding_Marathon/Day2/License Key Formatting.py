"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes.
The string is separated into n + 1 groups by n dashes. You are also given an integer k.
We want to reformat the string s such that each group contains exactly k characters, except for the first group,
which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash
inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

dashes_removed = str("".join([i for i in s if i != "-"]))
reversed = dashes_removed[::-1]
new_s = str("-".join([reversed[i:i+k] for i in range(len(reversed))]))
print(new_s)
"""


s = "2-5g-3-J"
k = 2
listed_val = [i for i in s if i != "-"][::-1]  #['w', '9', 'e', '2', 'Z', '3', 'F', '5']
#print(listed_val)
new_str = ""
for i in range(len(listed_val)//k + 1):
    new_str += "".join(listed_val[:k:])
    new_str += "-"                             #w9e2-Z3F5-
    listed_val = listed_val[k::]
reformatted = new_str[:-1:][::-1].upper()
print(new_str)
print(reformatted)


#to do check the case -5F3Z-2E9W








