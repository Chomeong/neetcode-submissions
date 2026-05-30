class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []

        if len(prices) <= 1:
            return 0
        else:
            for i in range(len(prices)):
                for j in range(i+1, len(prices)):
                    count_profit = prices[j] - prices[i]
                    profit.append(count_profit)
            if max(profit) < 0:
                return 0
            else:
                return max(profit)

        