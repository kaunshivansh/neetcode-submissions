class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def dfs(idx, path):
            if idx == len(digits):
                res.append(path)
                return

            for ch in phone[digits[idx]]:
                dfs(idx + 1, path + ch)

        dfs(0, "")
        return res