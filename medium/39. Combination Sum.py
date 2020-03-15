class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def backtrack(i, temp_target, temp):
            if temp_target > target or i == n:
                return 
            if temp_target == target:
                res.append(temp)
                return 
            
            backtrack(i, temp_target+candidates[i], temp+[candidates[i]])
            backtrack(i+1, temp_target, temp)
        
        backtrack(0, 0, [])

        return res
