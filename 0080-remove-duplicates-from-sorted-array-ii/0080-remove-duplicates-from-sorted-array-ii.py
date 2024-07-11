class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        if len(nums) <= 2:
            return len(nums)
        
        write_index = 2  # Start writing from the third position

        for read_index in range(2, len(nums)):
            if nums[read_index] != nums[write_index - 2]:
                nums[write_index] = nums[read_index]
                write_index += 1

        return write_index




            
