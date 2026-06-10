from typing import List

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        new_edges = []
        for i, (u, v, w) in enumerate(edges):
            new_edges.append([u, v, w, i])

        new_edges.sort(key=lambda x: x[2])

        class DSU:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, a, b):
                pa, pb = self.find(a), self.find(b)

                if pa == pb:
                    return False

                if self.rank[pa] < self.rank[pb]:
                    pa, pb = pb, pa

                self.parent[pb] = pa

                if self.rank[pa] == self.rank[pb]:
                    self.rank[pa] += 1

                return True

        def mst(exclude=-1, include=-1):
            dsu = DSU(n)
            weight = 0
            edges_used = 0

            if include != -1:
                u, v, w, _ = new_edges[include]
                dsu.union(u, v)
                weight += w
                edges_used += 1

            for i, (u, v, w, _) in enumerate(new_edges):
                if i == exclude:
                    continue

                if dsu.union(u, v):
                    weight += w
                    edges_used += 1

            return weight if edges_used == n - 1 else float('inf')

        base_mst = mst()

        critical = []
        pseudo = []

        for i in range(len(new_edges)):
            if mst(exclude=i) > base_mst:
                critical.append(new_edges[i][3])
            elif mst(include=i) == base_mst:
                pseudo.append(new_edges[i][3])

        return [critical, pseudo]