from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)

        checks = (len(s2)-len(s1)+1)

        for i in range (checks):
            s2_counter = Counter(s2[i: i+len(s1)])
            if s2_counter == s1_counter:
                return True
        
        return False




                