class Solution:
        
    def encode(self, strs: List[str]) -> str:
        ar = []
        for a in strs:
            tam = len(a)

            ar.append(str(tam))
            ar.append('#')
            ar.append(a)
        return "".join(ar)
        
            
    def decode(self, s: str) -> List[str]:
        res = []
        a = 0

        while a < len(s):
            j = a
            while s[j] is not '#':
                j = j + 1
            tama = int(s[a:j])
            a = j + 1
            j = a + tama
            res.append(s[a:j])
            a = a + tama

        return res