class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # fixed window problem
        # number_met += (if average(window) >= threshold)

        num_sub_arrays = 0
        # instead of calculating the sum each time, we can keep a running sum
        running_sum = sum(arr[0:k])

        if (running_sum)/k >= threshold:
            num_sub_arrays+=1

        for left in range(1,len(arr)-k+1):
            # remove the previous sum and add the next one
            running_sum -= arr[left-1]
            running_sum += arr[left+k-1]

            if (running_sum)/k >= threshold:
                num_sub_arrays += 1
        return num_sub_arrays