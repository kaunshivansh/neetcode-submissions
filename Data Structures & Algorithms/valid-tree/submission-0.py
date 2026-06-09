from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
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
                return False

            if rank[pa] < rank[pb]:
                pa, pb = pb, pa

            parent[pb] = pa
            rank[pa] += rank[pb]
            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True