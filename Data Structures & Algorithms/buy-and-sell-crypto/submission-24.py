class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        olg = 0
        l = prices[0]
        for r in range(len(prices)):
            olg = max(olg, prices[r] - l)
            l = min(l,prices[r])
        return olg

