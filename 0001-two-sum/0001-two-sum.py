class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict1 = {}

        for index, element in enumerate(nums):

            Looking4 = target - element

            if Looking4 in dict1:
                return [dict1[Looking4],index]

            else:

                dict1[element] = index



        
        