from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # goal: find a range : sliding window
        # desired length of that window, fixed window

        # inital: track of how many black and how many white
        # move window each by one time (remove and add from that count)
        # get: minumum number of white blocks to turn into

        
        move = len(blocks) - k + 1
        window_freq = Counter(blocks[0:k])
        minimum = window_freq["W"]

        for left in range(1, move):
            # add and remove 
            window_freq[blocks[left-1]] -=1
            window_freq[blocks[left+k-1]] += 1

            minimum = min(minimum, window_freq["W"])
            print(window_freq)
        
        return minimum



        