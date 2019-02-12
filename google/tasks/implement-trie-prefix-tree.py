# https://www.lintcode.com/problem/implement-trie-prefix-tree/description

class Node:

    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.is_word_end = False

    def add_child(self, node):
        self.children[node.letter] = node


class Trie:

    def __init__(self):
        # do intialization if necessary
        self.root = Node(None)

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                letter_node = Node(letter)
                node.add_child(letter_node)
                node = letter_node
        node.is_word_end = True

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_word_end

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True