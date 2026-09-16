class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # from this to that, we need to get a range (window)
        # if no profit -> nothing
        # the window size is changing

        # brute force: check every possible combination
        # sliding window:
        # point1 at 10, point2 at 1
        # when to advance left pointer: if the next number is smaller 
        # when to advance right pointer: if the next pointer is bigger (keep checking)

        # when do i know which pointer to move when?
        # looking into what it would be for each option? ehh

        buy = 0
        profit = 0

        for sell in range(1, len(prices)):
            actualprofit = prices[sell] - prices[buy]
            if (actualprofit) > profit:
                profit = actualprofit
            
            if prices[sell] < prices[buy]:
                print("here")
                buy = sell
        
        return profit

            

