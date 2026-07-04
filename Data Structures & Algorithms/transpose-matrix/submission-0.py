class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        
        # Create result matrix with swapped dimensions
        result = [[0] * m for _ in range(n)]
        
        # Fill the transposed values
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]
        
        return result