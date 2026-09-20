class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        col = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        	
        for i in range(9):
            for a in range(9):
                
                if board[i][a] == '.':
                    continue

                if board[i][a] in rows[i] or board[i][a] in col[a] or board[i][a] in squares[(i//3,a//3)]:
                    return False


                rows[i].add(board[i][a])
                col[a].add(board[i][a])
                squares[(i//3,a//3)].add(board[i][a])


        return True
