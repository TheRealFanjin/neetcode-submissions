class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        found = False
        word_idx = 0

        def search(node, word_idx):
            nonlocal found
            if word_idx == len(word) - 1:
                eow_in_children = False
                for child in node.children:
                    if node.children[child].end_of_word:
                        eow_in_children = True
                if (word[word_idx] == '.' and node.children and eow_in_children) or (word[word_idx] in node.children and node.children[word[word_idx]].end_of_word):
                    found = True
                return
            
            if word[word_idx] == '.':
                for child in node.children:
                    search(node.children[child], word_idx + 1)
            elif word[word_idx] in node.children:
                search(node.children[word[word_idx]], word_idx + 1)
            else:
                return
        
        search(self.root, word_idx)
        return found