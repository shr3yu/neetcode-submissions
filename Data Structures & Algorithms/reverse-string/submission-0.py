class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # brute force: for 1/2 the array switch the two

        for i in range(len(s)//2):
            a = s[i]
            s[i] = s[len(s)-1-i]
            s[len(s)-1-i] = a


        