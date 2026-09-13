class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <=1: 
            return nums

        middle = len(nums)//2
        
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])

        return self.merge(left, right)

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right): 
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            elif left[i] > right[j]:
                result.append(right[j])
                j+=1
            else:
                result.append(left[i])
                result.append(right[j])
                i+=1
                j+=1
        
        #left over
        while i < len(left):
            result.append(left[i])
            i+=1
        while j < len(right):
            result.append(right[j])
            j+=1
        
        return result
