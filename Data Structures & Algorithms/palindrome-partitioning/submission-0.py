class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        def backtrack(start):
            if start == len(s):
                result.append(list(path))
                return
            for i in range(start, len(s)):
                substring = s[start : i + 1]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(i + 1)
                    path.pop()
        def is_palindrome(sub):
            return sub == sub[::-1]

        backtrack(0)
        return result