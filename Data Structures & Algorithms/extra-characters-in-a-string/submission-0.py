from typing import List
from functools import lru_cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        n = len(s)

        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0

            ans = 1 + dfs(i + 1)

            for j in range(i, n):
                if s[i:j + 1] in words:
                    ans = min(ans, dfs(j + 1))

            return ans

        return dfs(0)