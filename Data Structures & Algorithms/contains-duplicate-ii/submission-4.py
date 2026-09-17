class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # lets use a set for our window
        window = set()

        # for any sliding window problem we need a left
        left = 0

        # go through every element
        # how do we regulate the size? remove the left side when youre done checking

        for right in range (len(nums)):
            
            # check if its in window
            if nums[right] in window:
                return True
            
            window.add(nums[right])

            # make sure the window does not go above k
            if len(window) > k:
                window.remove(nums[left])
                left+=1


        return False
        

        