class Solution:
    def reverse(self,x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        rev_x = 0
        
        while x != 0:
            digit = x % 10
            rev_x = rev_x * 10 + digit
            x //= 10
        
        rev_x *= sign
        
        if not (-2**31 <= rev_x <= 2**31 - 1):
            return 0
        
        return rev_x