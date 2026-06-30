import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        busy_rooms = []  # (end_time, room)
        count = [0] * n
        
        for start, end in meetings:
            # Free up rooms that have finished by 'start'
            while busy_rooms and busy_rooms[0][0] <= start:
                time, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
            else:
                time, room = heapq.heappop(busy_rooms)
                duration = end - start
                heapq.heappush(busy_rooms, (time + duration, room))
            
            count[room] += 1
        
        return count.index(max(count))