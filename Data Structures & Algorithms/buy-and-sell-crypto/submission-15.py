class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        olg=0

        while r < len(prices):

            if prices[l] == prices[r]:
                r=r+1
            elif prices[l] < prices[r]:
                olg= max(olg , prices[r]-prices[l])
                print(prices[r]-prices[l])

                r=r+1
                

            elif prices[l] > prices[r]:
                l = r
            


        return olg

