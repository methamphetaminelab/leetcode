import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        aplhabet, digits = string.ascii_lowercase, string.digits
        result = ''

        for i in s.lower():
            if i in aplhabet or i in digits:
                result += i
        
        return True if result == result[::-1] else False