class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for tok in tokens:
            if tok == "+":
                result = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tok == "-":
                result = (stack[-2] - stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tok == "*":
                result = (stack[-1] * stack[-2])
                
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tok == "/":
                result = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(int(tok))


        return stack.pop()


