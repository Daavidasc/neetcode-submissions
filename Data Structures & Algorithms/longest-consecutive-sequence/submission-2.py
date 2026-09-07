class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxsum=1
        s = set()
        if not nums:
            return 0
        for a in nums:
            s.add(a)
        for a in nums:
            if a - 1 not in s:
                aux = 1
                while a + aux in s:
                    aux = aux + 1
                    if maxsum<aux:
                        maxsum = aux


        return maxsum