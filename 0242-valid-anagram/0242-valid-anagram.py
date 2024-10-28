class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict1 = {}
        dict2 = {}


        for letter in s:

            if letter not in dict1:
                dict1[letter] = s.count(letter)


        for letter in t:

            if letter not in dict2:
                dict2[letter] = t.count(letter)


        if dict1 == dict2:
            return True
        else:
            return False
            