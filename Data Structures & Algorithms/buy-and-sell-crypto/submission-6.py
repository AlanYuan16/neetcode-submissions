class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two point L:Buy R:Sell
        l, r = 0, 1
        max_p = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                max_p = max(max_p, p)
            else: 
                l = r
            r += 1
        return max_p