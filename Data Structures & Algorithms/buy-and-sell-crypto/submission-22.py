class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        olg = 0
        mini = prices[0]
        for price in prices:
            olg=max(olg, price-mini)
            mini = min(price,mini) 

        return olg

