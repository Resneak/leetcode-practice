class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []  # This will store tuples of (count, previous string state)
        tempCount = ""
        tempString = ""

        for c in s:
            if c.isdigit():
                tempCount += c

            elif c == '[':
                # Push the current count and tempString to the stack
                stack.append((int(tempCount), tempString))
                tempCount = ""      # Reset tempCount for the next number
                tempString = ""      # Reset tempString for the nested string

            elif c == ']':
                # Pop the last (count, previous string state) from the stack
                PrevTemps = stack.pop()
                repeat_count = PrevTemps[0]
                prev_string = PrevTemps[1]

                # Update tempString: decoded current part + previous state
                tempString = prev_string + (tempString * repeat_count)

            else:
                # Add characters to tempString
                tempString += c

        return tempString

        



