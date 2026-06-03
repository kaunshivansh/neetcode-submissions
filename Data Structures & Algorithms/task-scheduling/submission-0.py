from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        max_heap = [-freq for freq in count.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown = deque()  # [remaining_count, available_time]

        while max_heap or cooldown:
            time += 1

            if max_heap:
                freq = 1 + heapq.heappop(max_heap)
                if freq:
                    cooldown.append((freq, time + n))

            if cooldown and cooldown[0][1] == time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        return time