class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1  # we already have first number = x
        result = x
        
        bit = 0
        while n > 0:
            # If this bit is not set in x, we can use it
            if (x & (1 << bit)) == 0:
                # Fill this bit from n
                if n & 1:
                    result |= (1 << bit)
                n >>= 1
            bit += 1
        
        return result