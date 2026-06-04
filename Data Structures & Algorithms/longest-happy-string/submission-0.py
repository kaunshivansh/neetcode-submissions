from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a:
            heappush(heap, (-a, 'a'))
        if b:
            heappush(heap, (-b, 'b'))
        if c:
            heappush(heap, (-c, 'c'))

        res = []

        while heap:
            cnt1, ch1 = heappop(heap)

            if len(res) >= 2 and res[-1] == res[-2] == ch1:
                if not heap:
                    break

                cnt2, ch2 = heappop(heap)

                res.append(ch2)
                cnt2 += 1

                if cnt2:
                    heappush(heap, (cnt2, ch2))
                heappush(heap, (cnt1, ch1))
            else:
                res.append(ch1)
                cnt1 += 1

                if cnt1:
                    heappush(heap, (cnt1, ch1))

        return ''.join(res)