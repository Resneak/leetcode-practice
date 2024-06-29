class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        emptydict = {}
        for element in nums:

            if element not in emptydict:
                emptydict[element] = 1

            else:
                emptydict[element] = emptydict[element] + 1

        return max(emptydict, key=emptydict.get)
