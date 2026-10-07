class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r

        while l <= r:
            mid = (l +r) //2

            total = 0
            for p in piles:
                total = total + math.ceil(p/mid)

            if total <= h:
                r = mid - 1
                res = mid
            else:
                l = mid+1
        return res