

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def build(r, c, size):
            first = grid[r][c]
            uniform = True

            for i in range(r, r + size):
                for j in range(c, c + size):
                    if grid[i][j] != first:
                        uniform = False
                        break
                if not uniform:
                    break

            if uniform:
                return Node(bool(first), True, None, None, None, None)

            half = size // 2

            topLeft = build(r, c, half)
            topRight = build(r, c + half, half)
            bottomLeft = build(r + half, c, half)
            bottomRight = build(r + half, c + half, half)

            return Node(
                True,        
                False,
                topLeft,
                topRight,
                bottomLeft,
                bottomRight
            )

        return build(0, 0, len(grid))