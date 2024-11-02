class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        dict1 = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        for char in s:
            if char in dict1.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                elif stack[-1] == dict1[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

