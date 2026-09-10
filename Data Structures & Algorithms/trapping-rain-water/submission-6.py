class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height)-1
        maxl = height[l]
        maxr = height[r]
        agua = 0
        while l<=r:
            if maxl<maxr:
                if(maxl<height[l]):
                    maxl = height[l]    
                agua = agua + maxl - height[l]
                l=l+1

                
            else:
                if(maxr<height[r]):
                    maxr = height[r]
                agua = agua + maxr - height[r]
                r=r-1

                


            

        return agua