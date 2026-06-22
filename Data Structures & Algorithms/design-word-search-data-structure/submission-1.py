class WordDictionary:

    def __init__(self):
        self.children = {}
        self.EOW = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children: 
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.EOW = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.EOW
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            if char not in node.children:
                return False
            return dfs(index + 1, node.children[char])
        return dfs(0, self)