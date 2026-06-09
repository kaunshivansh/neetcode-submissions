from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        q = deque([("0000", 0)])
        visited = {"0000"}

        while q:
            state, moves = q.popleft()

            if state == target:
                return moves

            for i in range(4):
                digit = int(state[i])

                for delta in (-1, 1):
                    nd = (digit + delta) % 10

                    nxt = (
                        state[:i]
                        + str(nd)
                        + state[i + 1:]
                    )

                    if nxt not in dead and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, moves + 1))

        return -1