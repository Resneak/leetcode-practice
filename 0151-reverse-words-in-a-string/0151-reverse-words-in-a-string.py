class Solution:
    def reverseWords(self, s: str) -> str:

        splitstrings = s.split(' ')
        print(splitstrings)


        emptyList = ""

        wordcount = 0
        for index, word in enumerate(reversed(splitstrings)):
            if word == '':
                pass
            else:
                
                if wordcount != 0:
                    emptyList = emptyList + " " + word
                else:
                    emptyList = emptyList + word
                wordcount = wordcount + 1
                

        return emptyList



        