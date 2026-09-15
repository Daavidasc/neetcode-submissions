class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        olg = 0
        l = 0
        for r in range(len(prices)):
            if prices[r]>prices[l]:
                olg = max(olg, prices[r] - prices[l])
            elif prices[l]>prices[r]:
                    l = r
        return olg

