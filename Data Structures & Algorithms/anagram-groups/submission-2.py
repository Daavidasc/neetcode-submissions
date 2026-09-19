class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}

        for a in strs:
            temp = "".join(sorted(a))
            if temp not in s:
                s[temp] = []
            s[temp].append(a)
    
        return list(s.values())