class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s + ' '
        x = s.split(' ')
        Xrev = list(reversed(x))

        for index, element in enumerate(Xrev):
            if element != '':
                indexOfLastWord = index
                print(f"index of last word: {indexOfLastWord}")
                break
        
        lastword = Xrev[indexOfLastWord]
        lastwordlength = len(lastword)
        return lastwordlength