from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap method
        # we need to know how much of each value there is

        seen = defaultdict(int)
        for num in nums:
            seen[num] +=1 
        
        # put them into an array so we can order them
        arr = []
        for num, cnt in seen.items():
            arr.append([cnt,num])

        #now we have everything in an array, lets sort, and pop off n-k elements
        result = []
        arr.sort() # small -> big
        for i in range (k):
            result.append(arr.pop()[1])

        return result



            



