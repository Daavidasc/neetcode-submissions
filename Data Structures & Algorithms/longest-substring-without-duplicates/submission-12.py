class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        se = {}
        maxlen = 0
        l = 0

        for d in range(len(s)):
            if s[d] in se:
                l = max(se[s[d]]+1, l)
            se[s[d]] = d
            maxlen = max(maxlen,(d-l) +1) 
            
        return maxlen

            
