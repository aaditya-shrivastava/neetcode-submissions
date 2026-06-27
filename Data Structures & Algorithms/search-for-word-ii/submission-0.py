class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
            node.word = word
        rows, cols = len(board), len(board[0])
        result = set()
        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] not in node.children:
                return
            char = board[r][c]
            next_node = node.children[char]
            if next_node.is_end_of_word:
                result.add(next_node.word)
            board[r][c] = '#'
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)
            board[r][c] = char 
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return list(result)