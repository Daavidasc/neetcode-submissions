class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(',
        '}':'{',
        ']':'['}

        arr = []

        for a in s:
            if a in dic:
                if arr and dic[a] == arr[-1]:
                    arr.pop()
                else: 
                    return False  
            else:    
                arr.append(a)

        if arr:
            return False
        return True 

                