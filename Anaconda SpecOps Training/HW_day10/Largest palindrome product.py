"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
lst_product = []
i_j_nums = []
for i in range(1000, 100, -1):
    for j in range(1000, 100, -1):
        product = i * j
        if list(str(product)) == list(str(product))[::-1]:
            lst_product.append(product)
            i_j_nums.append([i, j])

max_palindrome = max(lst_product)
print(i_j_nums[lst_product.index(max_palindrome)])





