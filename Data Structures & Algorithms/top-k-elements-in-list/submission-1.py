class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        bucket = [[] for _ in range(len(nums)+1)]
        
        for n in nums:
            s[n]=s.get(n,0)+1
        
        

        for key, num in s.items():
            bucket[num].append(key) 

        winer = []
        for num in range(len(nums),0,-1):
            for n in bucket[num]:
                winer.append(n)
                if len(winer)==k:
                    return winer