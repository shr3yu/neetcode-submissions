class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # sorted in increasing order 
        insert = m+n-1
        val2 = n-1
        val1 = m-1

        for i in range (m+n):
            if val2 < 0:
                nums1[insert] = nums1[val1]
                val1-=1
                
            elif val1<0:
                nums1[insert] = nums2[val2]
                val2-=1
                
            else: 
                maxum = max(nums1[val1], nums2[val2])
                nums1[insert] = maxum
                if maxum == nums1[val1]:
                    val1-=1
                else:
                    val2-=1
            insert-=1

            #decrement the val1 or val2
            

        


