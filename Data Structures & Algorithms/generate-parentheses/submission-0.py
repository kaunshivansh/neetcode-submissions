class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_cnt, close_cnt, path):
            if len(path) == 2 * n:
                res.append(path)
                return

            if open_cnt < n:
                dfs(open_cnt + 1, close_cnt, path + "(")

            if close_cnt < open_cnt:
                dfs(open_cnt, close_cnt + 1, path + ")")

        dfs(0, 0, "")
        return res       