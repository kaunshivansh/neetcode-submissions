from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = list(range(n + 1))
        rank = [1] * (n + 1)

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
                return [u, v]