class Solution:
    def maxArea(self, heights: List[int]) -> int:
            l = 0
            r = len(heights) - 1
            maxi = 0

            while l < r:
                maxi = max(maxi, (r - l) * min(heights[l], heights[r]))

                if heights[l] > heights[r]:
                    r = r-1
                    
                else:
                    l = l + 1


            return maxi

