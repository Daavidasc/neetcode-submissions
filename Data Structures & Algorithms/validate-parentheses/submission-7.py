class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', 
                ']':'[',
                '}':'{'}
        stack = []
        for a in s:
            if a in dic:
                if stack and dic[a] == stack[-1]: 
                    stack.pop()
                else:
                    return False
            else:         
                stack.append(a)

        if stack == []:
            return True
        else:
            return False

                