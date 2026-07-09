class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Reverse both strings for easier calculation
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(m):
            for j in range(n):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                result[i + j] += digit1 * digit2
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Remove leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Convert result to string
        return ''.join(map(str, result[::-1]))