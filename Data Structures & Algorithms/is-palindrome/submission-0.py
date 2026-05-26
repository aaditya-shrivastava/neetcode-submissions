class Solution:
    def isPalindrome(self, s: str) -> bool:
        sClean = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return sClean == sClean[::-1]