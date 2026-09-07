class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxsum=1
        s = set()
        if not nums:
            return 0
        for a in nums:
            s.add(a)
        for a in nums:
            aux = 1
            if a - 1 not in s:
                for e in range(len(nums)):
                    if a + 1 in s:
                        aux = aux + 1
                        a = a + 1
                        if maxsum<aux:
                            maxsum = aux
                    else:
                        break

        return maxsum