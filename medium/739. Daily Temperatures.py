class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = [[0, T[0]]]
        for i, temp in enumerate(T):
            while len(stack) > 0 and stack[-1][1] < temp:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
                
            stack.append([i, temp])            
        
        return res
