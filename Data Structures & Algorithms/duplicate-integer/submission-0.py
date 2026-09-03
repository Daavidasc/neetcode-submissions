class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visto = set()
        for n in nums:
            if n in visto:
                return True
            visto.add(n)
        return False
