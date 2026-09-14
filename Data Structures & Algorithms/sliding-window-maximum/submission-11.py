class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k > len(nums):
            return False

        res = []
        dic = { }
        l = 0

        for r in range(k):
            dic[nums[r]] = 1 + dic.get(nums[r],0)
        res.append(max(dic))

        for r in range(k, len(nums)):

            dic[nums[r]] = 1 + dic.get(nums[r],0)
            dic[nums[l]] = dic[nums[l]] - 1
            if dic[nums[l]] == 0:
                del dic[nums[l]]
            l += 1
            if k == 1: print(dic)
            res.append(max(dic))


        return res