class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l =0
        d = len(heights)-1
        maxArea = 0
        
        while l<d:
            aux = min(heights[l], heights[d])
            if maxArea <aux*(d-l):
                maxArea= aux*(d-l)
            
            if heights[l] < heights[d]:
                l= l+1
            else:
                d=d-1
        return maxArea

