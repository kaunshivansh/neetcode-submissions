class Solution:
    def partitionLabels(self, s: str):
        # store last occurrence of each character
        last = {ch: i for i, ch in enumerate(s)}
        
        result = []
        start = end = 0
        
        # iterate through string
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            
            # when current partition ends
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result