class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False 

        matches = {
            "(": ")",
            "{": "}",
            "[": "]",
        }

        stack = [] 

        for i in s: 
            if i in matches:
                stack.append(i)
            else: 
                if not stack or matches[stack[-1]] != i:
                    return False
                stack.pop()
        
        if not stack: 
            return True
        else: 
            return False
                
