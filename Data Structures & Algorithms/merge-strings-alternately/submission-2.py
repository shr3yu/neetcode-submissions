class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        minlen= min(len1, len2)
        maxword = word1 if len1 > len2 else word2
        
        together = ""

        for i in range (minlen):
            together += word1[i]
            together += word2[i]
        
        for i in range (minlen, len(maxword)):
            together += maxword[i]
        
        return together
        

            
        