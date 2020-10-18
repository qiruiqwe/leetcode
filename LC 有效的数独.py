# @Time : 2020/10/18 23:19
# @Author : 亓瑞
# @File : LC 有效的数独.py
# @desc :
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 1. 行中1-9没有重复
        if self.check(board, 0, 0, 9) != True:
            return False
        # 2. 列中1-0没有重复
        hashtable = set()
        for i in range(9):
            for j in range(9):
                if board[j][i] == '.':
                    continue
                elif board[j][i] in hashtable:
                    print(i, j, hashtable, board[j][i])
                    return False
                else:
                    hashtable.add(board[j][i])
            hashtable.clear()
        # 3. 3*3中1-9没有重复
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if self.check(board, i, j, 3) != True:
                    return False
        return True

    def check(self, board, row, clu, step):
        hashtable = set()
        for i in range(row, row+step):
            for j in range(clu, clu+step):
                if board[i][j] == '.':
                    continue
                elif board[i][j] in hashtable:
                    print(1)
                    print(i, j, hashtable, board[i][j])
                    return False
                else:
                    hashtable.add(board[i][j])
            if step == 9:
                hashtable.clear()
        hashtable.clear()
        return True





a = [[".",".",".",".","5",".",".","1","."],
     [".","4",".","3",".",".",".",".","."],
     [".",".",".",".",".","3",".",".","1"],
     ["8",".",".",".",".",".",".","2","."],
     [".",".","2",".","7",".",".",".","."],
     [".","1","5",".",".",".",".",".","."],
     [".",".",".",".",".","2",".",".","."],
     [".","2",".","9",".",".",".",".","."],
     [".",".","4",".",".",".",".",".","."]]
b = [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(b))
