class Solution:
    def merge(self, intervals):
        # Step 1: Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If merged list is empty OR no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping → merge intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged