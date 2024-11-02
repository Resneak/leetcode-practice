class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        final = ""

        for c in s:

            if c == ']': # 3,[,a
                isDigit = False
                tempMultiply = ""
                tempString = ""
                while True:
                    
                    if not stack:
                        break

                    print(stack)

                    unknown = stack.pop()

                    if unknown.isdigit():
                        if isDigit == False:
                            isDigit = True

                        tempMultiply = unknown + tempMultiply # "3"
                    
                    elif isDigit == True and not unknown.isdigit():
                        stack.append(unknown)
                        break

                    elif unknown == '[':
                        pass

                    else:
                        tempString = unknown + tempString # "a"

                print(tempMultiply)
                print(tempString)

                final4brackets = int(tempMultiply) * tempString

                if stack:
                    stack.append(final4brackets)
                else:
                    final = final + final4brackets
                    

            else:
                stack.append(c)

        toAdd = ""
        while stack:
            toAdd = stack.pop() + toAdd

        return final + toAdd