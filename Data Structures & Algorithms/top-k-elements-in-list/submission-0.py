class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for n in nums:
            s[n]=s.get(n,0)+1
        top_n_claves = sorted(s, key=s.get, reverse=True)[:k]
        return top_n_claves