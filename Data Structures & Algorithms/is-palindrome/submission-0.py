class Solution:
    def isPalindrome(self, s):
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]