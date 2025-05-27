class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        if left == right and top == bottom:
            return matrix[top][left] == target

        while top <= bottom:
            midRow = (top + bottom) // 2

            if matrix[midRow][-1] >= target and matrix[midRow][0] <= target:
                break

            if matrix[midRow][-1] < target:
                top = midRow + 1
                continue

            if matrix[midRow][0] > target:
                bottom = midRow - 1

        if top > bottom:
            return False

        midRow = (top + bottom) // 2

        while left <= right:
            midCol = (left + right) // 2 

            if matrix[midRow][midCol] == target:
                return True

            if matrix[midRow][midCol] < target:
                left = midCol + 1
            else:
                right = midCol - 1

        return False
