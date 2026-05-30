class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print(len(matrix))
        for i in range(len(matrix)-1, -1, -1):
            if matrix[i][0] <= target:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
                return False
        return False