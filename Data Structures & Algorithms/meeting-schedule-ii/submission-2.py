import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x.start)

        min_heap = []

        # Add first meeting end time
        heapq.heappush(min_heap, intervals[0].end)

        for i in range(1, len(intervals)):
            start = intervals[i].start
            end = intervals[i].end

            # If earliest room is free
            if min_heap[0] <= start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

        return len(min_heap)