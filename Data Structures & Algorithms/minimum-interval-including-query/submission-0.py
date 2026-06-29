import heapq

class Solution:
    def minInterval(self, intervals, queries):
        # Sort intervals by start
        intervals.sort()

        # Sort queries with index
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        res = [-1] * len(queries)
        min_heap = []
        i = 0  # pointer for intervals

        for q, idx in sorted_queries:
            # Add all intervals starting before or at q
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                length = right - left + 1
                heapq.heappush(min_heap, (length, right))
                i += 1

            # Remove intervals that cannot cover q
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # Top of heap is the smallest valid interval
            if min_heap:
                res[idx] = min_heap[0][0]

        return res