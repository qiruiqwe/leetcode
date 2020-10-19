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
        for i in range(row, row + step):
            for j in range(clu, clu + step):
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

    def isValidSudoku2(self, board):
        '''
        通过一次遍历 完成三次遍历的工作
        :param board:
        :return:
        '''
        # 每一行使用set进行存储
        rows = [set() for _ in range(9)]
        # 每一列使用set进行存储
        columns = [set() for _ in range(9)]
        # 每3*3的小方块 建一个存储单位
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                temp = board[i][j]
                if temp == ".":
                    continue
                # 选择需要填入的块
                box_index = int(i // 3 * 3 + j // 3)
                if temp not in rows[i] and temp not in columns[j] and temp not in box[box_index]:
                    rows[i].add(temp)
                    columns[j].add(temp)
                    box[box_index].add(temp)
                else:
                    return False
        return True


a = [[".", ".", ".", ".", "5", ".", ".", "1", "."],
     [".", "4", ".", "3", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", "3", ".", ".", "1"],
     ["8", ".", ".", ".", ".", ".", ".", "2", "."],
     [".", ".", "2", ".", "7", ".", ".", ".", "."],
     [".", "1", "5", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", "2", ".", ".", "."],
     [".", "2", ".", "9", ".", ".", ".", ".", "."],
     [".", ".", "4", ".", ".", ".", ".", ".", "."]]
b = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."],
     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."],
     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku2(a))
