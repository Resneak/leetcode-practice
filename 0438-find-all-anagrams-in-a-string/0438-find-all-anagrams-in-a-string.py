class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        from collections import Counter

        Anagram_Dict = Counter(p)

        window = defaultdict(int)
        left = 0

        result = []

        for right in range(len(s)): # 0 1 2 3 4 5 6

            window[s[right]] += 1

            if right - left + 1 == len(p): # length matches p

                #print(s[left:right+1])

                #print(window)
                #print('-----')
                #print(Anagram_Dict)

                if window == Anagram_Dict: # match found
                    result.append(left)
                    #print('match found!')

                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

        return result






