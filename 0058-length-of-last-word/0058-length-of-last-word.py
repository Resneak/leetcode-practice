class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip()
        print(words)
        words = words.split(' ')
        length = len(words[-1])


        return length