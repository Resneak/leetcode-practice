class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Use defaultdict to automatically create lists for new keys
        anagram_dict = defaultdict(list)
        
        for phrase in strs:
            # Use sorted tuple as the key
            key = tuple(sorted(phrase))  # Sorting takes O(m log m) where m is the length of the string
            anagram_dict[key].append(phrase)

        # Convert the dictionary values to a list of lists for the result
        return list(anagram_dict.values())


            

            