class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        emptylist = []
        k = 0
        dupes = 0
        copyList = nums[:]
        list2pop = []


        for index, element in enumerate(copyList): # 1 1 2
            print(f"going in loop for element {element} | index {index}")
            emptylist.append(element)

            print(f"element {element} is in list {emptylist.count(element)} times!")
            if emptylist.count(element) > 1: # 
                
                print(f"index {index}")
                list2pop.append(element)
                dupes = dupes + 1

            else:
                k = k + 1
                print(f"k is {k}")

        for element in list2pop:
            nums.remove(element)

        for x in range(dupes):
            nums.append(0)

        print(nums)
        print(k)
        return k