class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx]
            ):
                return False

            temp = board[r][c]
            board[r][c] = "#"   # mark visited

            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            board[r][c] = temp   # backtrack
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False