class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #poping and removing from nums in place is risky

        #k = how many elements are not val
        k = 0

        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        
        return k