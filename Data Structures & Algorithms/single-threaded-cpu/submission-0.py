from heapq import heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((e, p, i) for i, (e, p) in enumerate(tasks))
        
        n = len(tasks)
        heap = []
        res = []
        time = 0
        i = 0

        while i < n or heap:
            if not heap:
                time = max(time, tasks[i][0])

            while i < n and tasks[i][0] <= time:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                i += 1

            p, idx = heappop(heap)
            time += p
            res.append(idx)

        return res