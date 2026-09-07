class Solution:
    def isPalindrome(self, s: str) -> bool:
     
        li=0
        ld= len(s)-1
        while ld>li:
            while ld>li and not self.isAlNum(s[li]):
                li = li+1
            while ld>li and not self.isAlNum(s[ld]):
                ld = ld-1
            if s[li].lower() != s[ld].lower():
                return False
            li = li + 1
            ld = ld - 1
        return True

    def isAlNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a')<= ord(c) <= ord('z') or
        ord('0')<= ord(c) <= ord('9'))
