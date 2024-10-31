class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        dict1 = {}

        for index, element in enumerate(nums):

            complement = target - element # 9 - 2 = 7

            if complement in dict1:
                return [index, dict1[complement]]
            
            else: # complement not in dictionary
                dict1[element] = index