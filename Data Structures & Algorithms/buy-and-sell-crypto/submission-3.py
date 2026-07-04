class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = prices[0]

        for n in prices:
            min_val = min(n, min_val)
            curr = n - min_val
            if curr > 0:
                max_profit = max(curr, max_profit)

        if max_profit > 0:
            return max_profit
        else:
            return 0