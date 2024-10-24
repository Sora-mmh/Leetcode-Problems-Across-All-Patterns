class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current["*"] = ""
        
    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        return "*" in current

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

    # Solution 2
    # def __init__(self):
    #     self.list = []

    # def insert(self, word: str) -> None:
    #     self.list.append(word)
        

    # def search(self, word: str) -> bool:
    #     return word in self.list

    # def startsWith(self, prefix: str) -> bool:
    #     idx = 0
    #     while idx < len(self.list):
    #         if self.list[idx].startswith(prefix):
    #             return True
    #         else:
    #             idx += 1
    #     return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
