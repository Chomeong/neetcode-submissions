class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0

        if len(prices) <= 1:
            return 0
        else:
            for i in range(len(prices)):
                for j in range(i+1, len(prices)):
                    count_profit = prices[j] - prices[i]
                    if count_profit > best_profit:
                        best_profit = count_profit
            return best_profit

        