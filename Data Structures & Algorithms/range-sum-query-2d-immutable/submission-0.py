class NumMatrix:

    def __init__(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.ps = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            for c in range(COLS):
                self.ps[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.ps[r][c + 1]
                    + self.ps[r + 1][c]
                    - self.ps[r][c]
                )

    def sumRegion(self, row1, col1, row2, col2):
        ps = self.ps

        return (
            ps[row2 + 1][col2 + 1]
            - ps[row1][col2 + 1]
            - ps[row2 + 1][col1]
            + ps[row1][col1]
        )