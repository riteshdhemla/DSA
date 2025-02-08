class TrieNode:
    def __init__(self:"TrieNode"):
        self.children : dict[int, TrieNode] = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s: str) -> None:
        node = self.root
        for c in s:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True


    def search(self, s: str) -> bool:
        node = self.root
        for c in s:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end


    def _delete(self, node:"TrieNode", s:str, depth:int) -> bool:
        if not node:
            return False
        if depth == len(s):
            if not node.is_end:
                return False
            node.is_end = False
            return len(node.children) == 0
        val = s[depth]
        if val in node.children:
            should_delete = self._delete(node.children[val], s, depth+1)
            if should_delete:
                del node.children[val]
                # prefix of  word does not belong to any other string
                return len(node.children) == 0 and not node.is_end
        return False
    
    def delete(self, s):
        self._delete(self.root, s, 0)
        
trie = Trie()
trie.insert("milk")
trie.insert("cream")
trie.insert("curd")
assert trie.search("milk") == True
assert trie.search("cream") == True
assert trie.search("creas") == False
trie.delete("cream")
assert trie.search("cream") == False

# from pytrie import StringTrie
# trie = StringTrie()
# trie["apple"] = True
# trie["app"] = True

# del trie["apple"]
# print("apple" in trie)
# print("app" in trie)
