class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # need: minimal length
        # condition: sum(window) >= target

        #how can we keep track of minimal lenngth
        mlen = len(nums)+ 1

        #how do we keep track of a window?
        #note: flex window, 2 pointers

        # how these pointers move
        # left: if the window has hit the condition 
        # right: if window has NOT hit the condition

        # running sum
        running_sum = 0

        left = 0
        for right in range (len(nums)):
            running_sum += nums[right]
            while running_sum >= target:
                #hit the condiiton
                mlen = min(mlen, right-left+1)
                running_sum -= nums[left]
                left +=1
    
        return mlen if mlen != (len(nums)+1) else 0

