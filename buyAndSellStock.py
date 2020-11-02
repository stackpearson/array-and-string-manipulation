# You are given the prices of a stock, in the form of an array of integers, prices. Let's say that prices[i] is the price of the stock on the ith day (0-based index). Assuming that you are allowed to buy and sell the stock only once, your task is to find the maximum possible profit (the difference between the buy and sell prices).

# Note: You can assume there are no fees associated with buying or selling the stock.

# Example

# For prices = [6, 3, 1, 2, 5, 4], the output should be buyAndSellStock(prices) = 4.

# It would be most profitable to buy the stock on day 2 and sell it on day 4. Thus, the maximum profit is prices[4] - prices[2] = 5 - 1 = 4.

# For prices = [8, 5, 3, 1], the output should be buyAndSellStock(prices) = 0.

# Since the value of the stock drops each day, there's no way to make a profit from selling it. Hence, the maximum profit is 0.

# For prices = [3, 100, 1, 97], the output should be buyAndSellStock(prices) = 97.

# It would be most profitable to buy the stock on day 0 and sell it on day 1. Thus, the maximum profit is prices[1] - prices[0] = 100 - 3 = 97.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer prices

# Guaranteed constraints:
# 1 ≤ prices.length ≤ 105,
# 1 ≤ prices[i] ≤ 106.

# [output] integer

# The maximum possible profit.

def find_diff(prices):
    diff_list = []

    for x in prices:
        for y in prices:
            diff_list.append(x-y)
    return sorted(diff_list, reverse=True)

def buyAndSellStock(prices):

    # Check to make sure prices do rise at some point during our array, if not return 0
    #need to find the two indicies where the difference between them is highest
    # loop over array subtracting

    # this is my starting point
    # for i in range(len(prices) -1):
    #     if prices[i+1] > prices[i]:
    #         return 'there is a solution'

    # return 0

    prices_len = len(prices)
    biggest_diff = prices[1] - prices[0]
    smallest_elm = prices[0]

    for i in range(1, prices_len):
        if (prices[i] - smallest_elm):
            biggest_diff = prices[i] - smallest_elm

        if (prices[i] < smallest_elm):
            smallest_elm = prices[i]

    if (biggest_diff < 1):
        return 0

    return biggest_diff
    

# print(buyAndSellStock([20, 15, 2, 1, 10]))
prices = [20, 15, 2, 0]
# prices_len = len(prices)
print(buyAndSellStock(prices))
# print(find_diff([20, 15, 2, 20]))