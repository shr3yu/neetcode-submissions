class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"}" : "{", "]": "[", ")": "("}
        stack = []
        for letter in s:
            if letter in matches:
                if len(stack) == 0:
                    return False
                elif matches[letter] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                # opening, we should pop onto the stack
                stack.append(letter)
            print(stack)
        
        return (len(stack) == 0)
                




        