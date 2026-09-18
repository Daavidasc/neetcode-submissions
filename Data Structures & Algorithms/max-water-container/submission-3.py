class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l= 0
        r= len(heights)-1
        maxi = 0
        while l<r:
            
            aux= (min(heights[l],heights[r])* (r-l))

            maxi = max(maxi, aux)
            if heights[l] < heights[r]:
                l = l+1
            else:
                r = r-1

            print(aux)
        return maxi

