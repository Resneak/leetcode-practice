class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        dict1 = defaultdict(list)

        # key as shift counts

        for phrase in strings:

            shift_pattern = []

            for i in range(1, len(phrase)): # 1, 2 | a b c
                difference = (ord(phrase[i]) - ord(phrase[i - 1])) % 26
                shift_pattern.append(difference)

            dict1[tuple(shift_pattern)].append(phrase)


        return list(dict1.values())




                

            # 97, 98, 99

            
            


