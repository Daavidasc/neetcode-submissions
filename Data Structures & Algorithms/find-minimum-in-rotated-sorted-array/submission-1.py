class Solution:

    

    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r= len(nums)-1
        col = []

        while l<r:

            med = l + (r-l)//2
            a = nums[med]

            if a > nums[r]:
                l = med +1
            else:
                r = med

        return nums[l]