class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.data.append(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        for i in self.data:
            if i == word:
                return True
        
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = len(prefix)
        for i in self.data:
            if i[:n] == prefix:
                return True

        return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
