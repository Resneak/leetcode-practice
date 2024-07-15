class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize MasterList with empty lists for each row
        MasterList = [[] for _ in range(numRows)]
        
        # Variables to track current row and direction
        current_row = 0
        going_down = False
        
        for char in s:
            # Append the character to the current row
            MasterList[current_row].append(char)
            
            # If we are at the top or bottom row, change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row
            current_row += 1 if going_down else -1
        
        # Join the characters in each row to form the final result
        result = ''.join([''.join(row) for row in MasterList])
        return result
