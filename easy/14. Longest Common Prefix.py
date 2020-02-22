class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if not strs:
            return prefix
        
        elif len(strs) == 1:
            return strs[0]

        else:
            # 先求出最小长度
            min_lenth = len(strs[0])
            for item in strs:
                if len(item) < min_lenth:
                    min_lenth = len(item)

            count = 0
            alphabet = []
            
            # 遍历所有单词的最小长度个字母并保存
            while count < min_lenth:
                for word in strs:
                    alphabet.append(word[count])
                
                count += 1
            
            # 求解公共部分
            count = 1
            for i in range(len(alphabet) - 1):
                if alphabet[i] == alphabet[i+1] and count < len(strs) - 1:
                    count += 1
                elif alphabet[i] == alphabet[i+1] and count == len(strs) - 1:
                    prefix += alphabet[i]
                    count = 0
                elif alphabet[i] != alphabet[i+1] and count == 0:
                    count += 1
                else:
                    break
            
            return prefix
