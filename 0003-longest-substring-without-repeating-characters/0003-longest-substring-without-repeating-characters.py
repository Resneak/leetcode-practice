class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        max_length = 0

        temp = set()

        for right in range(len(s)): # 0 1 2 3 4 5 6

            while s[right] in temp:
                temp.remove(s[left])
                left += 1

            temp.add(s[right]) # add character to set

            max_length = max(max_length, right - left + 1)

        return max_length


                
