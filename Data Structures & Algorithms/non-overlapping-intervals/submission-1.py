class Solution:
    def eraseOverlapIntervals(self, intervals):
        # Step 1: sort by end time
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = intervals[0][1]
        
        # Step 2: iterate through intervals
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if start < prev_end:
                # overlap → remove
                count += 1
            else:
                # no overlap → update end
                prev_end = end
        
        return count