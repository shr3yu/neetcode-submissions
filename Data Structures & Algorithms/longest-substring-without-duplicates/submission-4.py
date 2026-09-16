class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #substring: doesnt have repeating character

        # seen? set 
        seen = set()

        # longest seen window?
        longest = 0

        # how to keep track of where the window starts? 
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                # the set of string is in seen so, lets remove it, and 
                # we made it so that it would the the left one (NO WE DIDNT thats why we need a while)
                seen.remove(s[left])
                left +=1 
            
            seen.add(s[right])
            if len(seen) > longest:
                longest = len(seen)

        return longest
            
