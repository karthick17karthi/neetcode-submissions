class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            row=matrix[i]
            for j in range(len(row)):
                if(matrix[i][j]==target):
                    return True
        return False