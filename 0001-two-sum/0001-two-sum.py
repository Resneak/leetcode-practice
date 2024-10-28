class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #nums = nums.sort()

        for index1, x in enumerate(nums):

            for count in range(index1+1, len(nums)):

                y = nums[count]

                if x + y == target:
                    return [index1, count]
        