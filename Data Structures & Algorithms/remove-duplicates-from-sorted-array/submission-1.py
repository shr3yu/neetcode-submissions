class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [1,13,1,1,2,3]

        # if we want to overwrite then we would have
        # to shift them over

        # we can have two pointers: 1. where to insert
        # 2. which number to check 
        
        seen = set()

        insert = 0
        check = 0

        while check < len(nums):
            if nums[check] not in seen: 
                seen.add(nums[check])
                nums[insert] = nums[check]
                insert += 1
            # if its a duplicate dont advance the insert pointer
            check += 1
        return len(seen)

