class Solution:

    def encode(self, strs: List[str]) -> str:
        code = []
        for a in strs:
            code.append(str(len(a)))
            code.append("#")
            code.append(a)    
        return "".join(code)
    def decode(self, s: str) -> List[str]:
        code = []
        i = 0

        while i < len(s):
            j=i
            while s[j] != "#":
                j=j+1
            lenght = int(s[i:j])
            i=j+1
            j=i+lenght
            code.append(s[i:j])
            i=j


        
        return code