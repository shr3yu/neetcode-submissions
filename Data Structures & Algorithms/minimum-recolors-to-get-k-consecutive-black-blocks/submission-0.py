from collections import Counter
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # goal: find a range : sliding window
        # desired length of that window, fixed window

        # inital: track of how many black and how many white
        # move window each by one time (remove and add from that count)
        # get: minumum number of white blocks to turn into

        minimum = k + 1
        move = len(blocks) - k + 1
        for i in range(move):
            window_freq = Counter(blocks[i:i+k])
            minimum = min(minimum, window_freq["W"])
        
        return minimum



        