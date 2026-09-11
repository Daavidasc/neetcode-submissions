class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        se = set()
        maxlen = 0
        l = 0

        for d in range(len(s)):
            if s[d] in se:
                while s[l] != s[d]:
                    se.discard(s[l])
                    l = l+1
                l= l+1
            se.add(s[d])    
            maxlen = max(maxlen,(d - l)+1) 

            
        return maxlen

            
