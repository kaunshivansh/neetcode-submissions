class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask (to handle negative numbers)
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        while b != 0:
            # sum without carry
            temp = (a ^ b) & mask
            
            # carry
            b = ((a & b) << 1) & mask
            
            a = temp
        
        # if a is negative in 32-bit
        return a if a <= max_int else ~(a ^ mask)