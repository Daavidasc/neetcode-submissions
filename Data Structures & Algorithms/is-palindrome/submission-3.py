class Solution:
    def isPalindrome(self, s: str) -> bool:
     
        li=0
        ld= len(s)-1
        while ld>li:
            while ld>li and not s[li].isalnum():
                li = li+1
            while ld>li and not s[ld].isalnum():
                ld = ld-1
                continue
            if s[li].lower() != s[ld].lower():
                return False
            li = li + 1
            ld = ld - 1
        return True
