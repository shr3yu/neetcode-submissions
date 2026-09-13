from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majoritynum = 0
        actualnum = 0
        track = defaultdict(int)

        for num in nums:
            # add it to the dict
            track[num]+=1

            if track[num] > majoritynum:
                majoritynum = track[num]
                actualnum = num

        return actualnum
            
        