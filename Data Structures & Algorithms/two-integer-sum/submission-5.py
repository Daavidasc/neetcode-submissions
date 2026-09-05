class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s= set()

        for a in nums:
            s.add(a)

        for a in range(len(nums)):
            rest = target - nums[a]
            if rest in s:
                result = nums.index(rest)
                
                if result != a:
                    return sorted([a,result]) 


        