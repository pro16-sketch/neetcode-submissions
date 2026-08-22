class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:# Check rows
        for i in range(len(board)):
    
            seen = set()
    
            for j in range(len(board[i])):
        
                num = board[i][j]
        
                if num == ".":
                    continue
            
                if num not in seen:
                    seen.add(num)
                else:
                    return False


# Check columns
        for j in range(len(board[0])):
    
            seen = set()
    
            for i in range(len(board)):
        
                num = board[i][j]
        
                if num == ".":
                    continue
            
                if num not in seen:
                    seen.add(num)
                else:
                    return False


# Check 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
        
                seen = set()
        
                for x in range(3):
                    for y in range(3):
                
                        num = board[i + x][j + y]
                
                        if num == ".":
                            continue
                    
                        if num not in seen:
                            seen.add(num)
                        else:
                            return False


        return True
        