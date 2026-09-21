class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for n in range(len(nums)):
            if n > 0:
                if nums[n-1] == nums[n]:
                    continue
            l=n+1
            r=len(nums)-1
            target = -nums[n]
            while l<r:
                if nums[l] + nums[r] == target:
                    ans.append([nums[n],nums[l],nums[r]])
                    r = r-1
                    l= l+1
                    while l<r and nums[l] == nums[l-1]:
                        l = l+1
                elif nums[l] + nums[r] > target:
                    r = r-1
                else:
                    l = l+1

        return ans