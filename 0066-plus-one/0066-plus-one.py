class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        string = ""
        for element in digits:
            string = string + str(element)

        # 99
        string = int(string) + 1
        # 100
        string = str(string)
        
        newList = []
        for element in string:
            newList.append(int(element))

        digits = newList
        return digits

        



        








        