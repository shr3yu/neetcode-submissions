class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # window is a fixed size of k 
        # Goal: minumum = min(minimum, high(window) - min(window))

        # no need to preserve placement, lets sort the array 
        nums.sort() # acsedning
        minimum = nums[-1]

        for left in range(len(nums)- k+ 1):
            minimum = min(minimum, nums[left + k-1]- nums[left])
        
        return minimum

        