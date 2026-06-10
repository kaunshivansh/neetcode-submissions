from typing import List

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        if 1 in nums:
            return False

        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)

            if pa == pb:
                return

            if rank[pa] < rank[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            rank[pa] += rank[pb]

        factor_owner = {}

        for i, num in enumerate(nums):
            x = num
            factor = 2

            while factor * factor <= x:
                if x % factor == 0:

                    if factor in factor_owner:
                        union(i, factor_owner[factor])
                    else:
                        factor_owner[factor] = i

                    while x % factor == 0:
                        x //= factor

                factor += 1

            if x > 1:
                if x in factor_owner:
                    union(i, factor_owner[x])
                else:
                    factor_owner[x] = i

        root = find(0)

        for i in range(1, n):
            if find(i) != root:
                return False

        return True