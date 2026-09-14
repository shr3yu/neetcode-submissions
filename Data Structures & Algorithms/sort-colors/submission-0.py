class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # (0, low): 0
        # [low,mid): 1
        # (high:end):2

        low = 0
        scan = 0
        high = len(nums)-1

        while scan <= high: #once mid crosses over high we are done

            if nums[scan] == 0:
                #put it in the low region and move the low pointer
                nums[scan], nums[low] = nums[low], nums[scan]
                low +=1
                scan += 1 #can continue searching

            elif nums[scan] == 1:
                # middle region
                scan += 1 #keep searching no swapping to do
            else: 
                #high region
                nums[high], nums[scan] = nums[scan], nums[high]
                high-=1
                # scan stays same beacuse it has to look at what the new value is

                

        