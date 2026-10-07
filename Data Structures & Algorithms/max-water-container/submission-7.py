class Solution:
    def maxArea(self, heights: List[int]) -> int:
            l = 0
            r = len(heights)-1
            maxi = 0
            while l < r:

                maxi = max(maxi, (r- l) * min(heights[r], heights[l]))

                if heights[l] < heights[r]:
                    l=l+1
                else:
                    r=r-1

            return maxi

