class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for n in prices:
            buy = min(buy, n)
            curr_prof = n - buy
            profit = max(profit, curr_prof)
        return profit
