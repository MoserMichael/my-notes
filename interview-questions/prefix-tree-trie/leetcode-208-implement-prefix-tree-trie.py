# 208. Implement Trie (Prefix Tree)
# Medium
#A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
#Implement the Trie class:
#
#    Trie() Initializes the trie object.
#    void insert(String word) Inserts the string word into the trie.
#    boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
# 
#
#Example 1:
#
#Input
#["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
#Output
#[null, null, true, false, true, null, true]
#
#Explanation
#Trie trie = new Trie();
#trie.insert("apple");
#trie.search("apple");   // return True
#trie.search("app");     // return False
#trie.startsWith("app"); // return True
#trie.insert("app");
#trie.search("app");     // return True
#
# 
#
#Constraints:
#
#    1 <= word.length, prefix.length <= 2000
#    word and prefix consist only of lowercase English letters.
#    At most 3 * 104 calls in total will be made to insert, search, and startsWith.
#
#



class Node:
    def __init__(self):
        self.map_to_next = {}
        self.is_end_of_string = False

    def get_node(self, ch):
        return self.map_to_next.get(ch)

    def insert(self, ch):
        next = self.map_to_next.get(ch)
        if next is None:
            new_node = Node()
            self.map_to_next[ ch ] = new_node
            return new_node
        return next

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            cur = cur.insert(ch)

        cur.is_end_of_string = True


    def _search_prefix(self, word):
        cur = self.root
        for ch in word:
            cur = cur.get_node(ch)
            if not cur:
                return None
        return cur


    def search(self, word: str) -> bool:
        cur = self._search_prefix(word)
        if not cur:
            return False
        return cur.is_end_of_string

    def startsWith(self, prefix: str) -> bool:
        cur = self._search_prefix(prefix)
        if not cur:
            return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
