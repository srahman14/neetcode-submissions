class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        # tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # stack = [-220,"17","+","5","+"]
        
        for i in tokens:
            if i not in "+-/*": 
                stack.append(int(i)) 
                continue 
            
            val1 = stack.pop() 
            val2 = stack.pop()

            if i == "+":
                stack.append(val2+ val1)
            elif i == "-":
                stack.append(val2- val1)
            elif i == "*":
                stack.append(val2* val1)
            else: 
                stack.append(int(val2 / val1))

        return stack[0]
