class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxprofit = 0
        # for i in range(len(prices) - 1):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell = prices[j]
        #         profit = sell - buy
        #         maxprofit = max(maxprofit, profit)
        # print(maxprofit)
        # return maxprofit
        min_buy = 100000
        max_profit = 0
        for i in range(len(prices)):
            # have a min
            # then drape over the arr updating only the best profit
            min_buy = min(min_buy, prices[i])
            profit = prices[i] - min_buy
            max_profit = max(max_profit, profit)
        print(max_profit)
        return max_profit




        