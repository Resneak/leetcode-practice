class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []

        def backtrack(remaining_target, start):
            if remaining_target == 0:
                # equals target
                res.append(sol[:])
                return

            if remaining_target < 0:
                # No valid combination, return
                return
            

            for i in range(start, len(candidates)): # 0 1 2 3 
                sol.append(candidates[i])
                backtrack(remaining_target - candidates[i], i)
                sol.pop()




        backtrack(target, 0)
        return res