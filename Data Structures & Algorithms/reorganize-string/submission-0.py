from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        n = len(s)

        if max(freq.values()) > (n + 1) // 2:
            return ""

        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapify(heap)

        res = []
        prev_cnt, prev_ch = 0, ""

        while heap:
            cnt, ch = heappop(heap)

            res.append(ch)

            if prev_cnt < 0:
                heappush(heap, (prev_cnt, prev_ch))

            cnt += 1
            prev_cnt, prev_ch = cnt, ch

        return "".join(res)