class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        
        for i in range(len(strs)):
            count = [0] * 26
            for word in strs[i]:
                index = ord(word) - ord('a')
                count[index] += 1
            try:
                str_dict[tuple(count)].append(strs[i]) 
            except Exception:
                str_dict[tuple(count)] = []
                str_dict[tuple(count)].append(strs[i]) 
        
        res = []
        for i in str_dict:
            res.append(str_dict[i])
    
        return res
