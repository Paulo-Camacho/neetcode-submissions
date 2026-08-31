class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(len(prices) - 1):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                profit = sell - buy
                maxprofit = max(maxprofit, profit)
        print(maxprofit)
        return maxprofit



        