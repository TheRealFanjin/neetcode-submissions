class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        if curr_node.end_of_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        
        return True