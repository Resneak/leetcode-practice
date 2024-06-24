class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = number of elements in list that are not va
        k = 0

        listOfIndexToDelete = []
        # 3 2 2 3 | 3 = val
        for index, element in enumerate(nums):
            if element == val: # 3 ? 3
                k = k + 1
                listOfIndexToDelete.append(index)
            else:
                pass

        # k = 2
        # listOfIndexToDelete = [0,3]
        for x in range(k): # 0 1 
            value = listOfIndexToDelete[x]
            del nums[value] # nums = 2 2 
            for index, element in enumerate(listOfIndexToDelete):
                listOfIndexToDelete[index] = listOfIndexToDelete[index] - 1

        #for x in range(k):
        #    nums.append(51)
        
        


