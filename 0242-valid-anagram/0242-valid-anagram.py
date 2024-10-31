class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        from collections import Counter

        counts4s = Counter(s)

        counts4t = Counter(t)

        if counts4s == counts4t:
            return True

        else:
            return False
