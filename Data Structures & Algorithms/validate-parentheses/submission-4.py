class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', 
                ']':'[',
                '}':'{'}
        stack = []
        for a in s:
            if a in dic and stack != []: 
                
                aux = stack.pop()
                if dic[a] != aux:
                    return False
            else:         
                stack.append(a)

        if stack == []:
            return True
        else:
            return False

                