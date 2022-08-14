"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + 3^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + 3 + .....10)^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is . 3025 - 385
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
sum_of_squares_first_100 = 0
sum_of_first_100 = 0
for i in range(101):
    sum_of_squares_first_100 += i**2
    sum_of_first_100 += i

#print(sum_of_first_100**2)             #25502500
#print(sum_of_squares_first_100)        #338350

diff = sum_of_first_100**2 - sum_of_squares_first_100
print(diff)  #25164150

