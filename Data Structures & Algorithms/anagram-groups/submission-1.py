from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for word in strs:
            sorted_string = "".join(sorted(word))
            hashmap[sorted_string].append(word)

        # "sorted: values"
        result = []
        for key, values in hashmap.items():
            result.append(values)
        return result



                