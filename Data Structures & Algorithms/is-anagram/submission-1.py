class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for a in s:
            d[a]=d.get(a,0)+1

        for a in t:
            d[a]=d.get(a,0)-1


        return all(0 == v for v in d.values())