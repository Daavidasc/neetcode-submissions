class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        l= 0
        r= 0
        maxlen = 0
        while r < len(s):
            window[s[r]] = window[s[r]] +1
            if ((r-l)+1 - max(window.values())) <= k:
                maxlen = max(maxlen, (r-l)+1)
            else: 
                window[s[l]] = window[s[l]] -1
                l = l+1
            r = r +1
        return maxlen


                
