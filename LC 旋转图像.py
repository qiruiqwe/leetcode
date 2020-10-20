# @Time : 2020/10/19 18:22
# @Author : 亓瑞
# @File : LC 旋转图像.py
# @desc :
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        width = len(matrix)
        length = len(matrix[0])
        newMatrix = []
        for j in range(length):
            temp = []
            for i in reversed(range(0, width)):
                temp.append(matrix[i][j])
            newMatrix.append(temp)
        matrix = newMatrix
        return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(Solution().rotate(matrix))
