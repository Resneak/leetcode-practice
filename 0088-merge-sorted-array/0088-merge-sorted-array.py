class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        emptylist = []

        if m != 0:
            for element in range(m):
                print(f'appending {nums1[element]}')
                emptylist.append(nums1[element])

        if n != 0:
            for element in range(n):
                print(f'appending {nums2[element]}')
                emptylist.append(nums2[element])

        emptylist.sort()

        for element in range(m+n):
            nums1[element] = emptylist[element]

        
        