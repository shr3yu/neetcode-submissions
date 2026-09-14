class Solution:

    # you have to return a string
    # encode the lengths when you reach a # and theres a number right after, then it would be a valid string

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string = string + str(len(word)) + "#" + word

        print(string)
        return string

    #what if the strs has #int

    # "#5absc" -> it would get skipped not even processed beacuse another #int would be added before it
    def decode(self, s: str) -> List[str]:
        i = 0 #pointer
        result = []

        # "4#abcd4#1233"
        # the first char is always a number, keep it there and look for the next #

        while i < len(s):
            j = i
            while s[j] != "#": 
                # this account for multi digit values
                j += 1

            # that means we have the length (total length)
            length = int(s[i:j])
            result.append(s[j+1: j+1+length])
            i = j+1+length
        
        return result
                


            



