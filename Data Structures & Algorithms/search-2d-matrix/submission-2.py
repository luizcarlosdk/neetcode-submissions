class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_size = len(matrix)
        col_size = len(matrix[0])
        l, r = 0, row_size * col_size - 1

        while l <= r:
            middle = (l+r)//2
            row = middle // col_size
            column = middle % col_size

            if matrix[row][column] > target:
                r = middle - 1
            elif matrix[row][column] < target:
                l = middle + 1
            else:
                return True
        
        return False