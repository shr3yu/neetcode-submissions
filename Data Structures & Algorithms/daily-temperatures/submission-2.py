class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # store indices

        for index, temp in enumerate(temperatures):
            # the new value is bigger than everything in the stack
            while stack and temp > temperatures[stack[-1]]:
                in2 = stack.pop()
                result[in2] = index - in2
            stack.append(index) # need to find its thing


        
        return result

        







        