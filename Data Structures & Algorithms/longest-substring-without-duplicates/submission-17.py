class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        window = {}
        l = 0
        maxLen = 0
        for r in range(len(s)):
            if s[r] in window:
                l = max(l, window[s[r]]+1)
            window[s[r]]= r
            maxLen = max(maxLen, (r-l)+1)
        return maxLen
            
