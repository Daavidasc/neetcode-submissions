class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s= {}

        for a in range(len(nums)):
            rest = target - nums[a]
            if rest in s:
                return [s[rest],a] 
            s[nums[a]]=a


        