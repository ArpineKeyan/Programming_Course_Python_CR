"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

prices = [7, 1, 5, 3, 6, 4]
sorted_decreasing = True
for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        if prices[i] < prices[j]:
            sorted_decreasing = False

if sorted_decreasing:
    max_profit = 0
    print("No profit")
else:
    max_profit = prices[1] - prices[0]
    for i in range(1, len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]


print(max_profit)