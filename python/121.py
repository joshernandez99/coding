## O(n^2) Method
# def maxProfit(prices: list[int]) -> int:
#     maxProfit = 0
#     for i in range(len(prices) - 1):
#         for j in range(len(prices) - 1 - i):
#             profit = prices[j + i + 1] - prices[i]
#             maxProfit = max(maxProfit, profit)
#     return maxProfit

## O(n) Method using Kanades Algorithm
def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    minProfit = prices[0]
    for x in prices:
        minProfit = min(minProfit, x)
        maxProfit = max(maxProfit, x - minProfit)
    return maxProfit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))