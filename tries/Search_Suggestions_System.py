from typing import List

class TrieNode():
    def __init__(self):
        self.children = {}
        self.words = []
        self.num = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            if current.num < 3:
                current.words.append(word)
                current.num += 1
    
    def search(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        return current.words
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for word in products:
            trie.add(word)
        result, prefix = [], ""
        for char in searchWord:
            prefix += char
            result.append(trie.search(prefix))
        return result

        # Construct the tree of caracters given the products strings
        # root = {}
        # for product in products:
        #     current = root
        #     for char in product:
        #         # print(product, char, current)
        #         if char in current:
        #             current = current[char]
        #         else:
        #             current[char] = {}
        #             current = current[char]   
        #     current["*"] = ''
             
        
