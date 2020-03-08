class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s + " "
        stack, reverse = [], ""
        for i in s:
            stack.append(i)
            if i == " ":
                while stack:
                    reverse = reverse + stack.pop()
        
        return reverse[1:]

# 独创方法
class Solution:
    def reverseWords(self, s: str) -> str:
        count = 0
        dict = {}
        # 统计空格数
        for i in s:
            if i == ' ':
                dict[int(count)] = []
                count += 1
        
        dict[int(count)] = []

        # 每个单词单独记录
        count = 0
        for i in s:
            if i != ' ':
                dict[int(count)].append(i)
            elif i == ' ':
                count += 1

        string = ""

        for i in range(count+1):
            for word in dict[int(i)][::-1]:
                string += word
            string += ' '
        
        return string[:-1]

        
        


