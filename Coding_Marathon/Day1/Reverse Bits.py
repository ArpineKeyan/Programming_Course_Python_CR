"""
Reverse bits of a given 32 bits unsigned integer.
"""

n = "00000010100101000001111010011100"
n_reversed = n[::-1]
int_ = int(n_reversed, 2)
print(int_)