class Solution:

    

    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r= len(nums)-1
        res = nums[0]

        while l<=r:
            if nums[l] < nums[r]:
                return min(res,nums[l])

            mid = l + (r-l)//2
            res = min(res,nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return res