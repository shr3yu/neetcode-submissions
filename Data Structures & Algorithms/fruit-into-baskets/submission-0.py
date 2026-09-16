class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # find the top 2 most produced fruits to maximize the amount of fruit you get

        # you need a range where its only the top 2 fruits you chose: flex

        # in your window: keep track of the top 2 numbers
        # if a new fruit enters the window, discard untill your window only has 2 fruit

        #find maximum fruits 
        maximum_fruits = 1
        # can not reorder the array

        window = Counter() # {type: count}

        left = 0

        for right in range(len(fruits)):
            window[fruits[right]] +=1 

            while len(window) > 2:
                window[fruits[left]] -=1
                # make sure we dont have empty values in there
                if (window[fruits[left]]== 0):
                    del window[fruits[left]]
                left+=1

            maximum_fruits = max(maximum_fruits, right-left+1)

        return maximum_fruits

