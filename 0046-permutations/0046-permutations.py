class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, sol = [], []  # Store results and the current path

        def backtrack():
            if len(sol) == len(nums):  # If the path is a complete permutation
                res.append(sol[:])  # Add a copy of the current path to results
                return  # Stop further recursion

            for x in nums:  # Loop over all numbers
                if x not in sol:  # If the number is not yet used in the path
                    sol.append(x)  # Choose the number
                    backtrack()  # Recurse to explore further
                    sol.pop()  # Backtrack (undo the choice)

        backtrack()  # Start the recursion
        return res  # Return all collected permutations

            
