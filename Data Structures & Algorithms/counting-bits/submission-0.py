class Solution:
    def countBits(self, n: int) -> list[int]:
        result = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # i >> 1 removes the last bit
            # i & 1 checks if the last bit is 1
            result[i] = result[i >> 1] + (i & 1)
        
        return result   