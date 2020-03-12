class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        string = ""
        minimum = len(strs[0])

        for word in strs:
            if len(word) < minimum:
                minimum = len(word)
        
        count = 0
        for i in range(minimum):
            for word in strs:
                if strs[0][i] == word[i]:
                    count += 1
                
            if count == len(strs):
                string += strs[0][i]
            else:
                break
            count = 0

        return string 
