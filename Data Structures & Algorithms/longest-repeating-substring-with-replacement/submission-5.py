class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        window = {}
        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            while window[max(window, key = window.get)] + k - (r-l + 1) <0:
                window[s[l]] = window[s[l]] -1
                l = 1 + l
            

            maxLen = max(maxLen, r-l + 1)

        return maxLen
