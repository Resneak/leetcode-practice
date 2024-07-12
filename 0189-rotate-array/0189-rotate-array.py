class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for x in range(k):
            removed_element = nums.pop(-1)
            nums.insert(0,removed_element)

