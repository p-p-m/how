# https://www.lintcode.com/problem/implement-trie-prefix-tree/description
import string


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


class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """

    def kDistance(self, words, target, k):
        trie = Trie()
        string.ascii_lowercase
        # trie


["abc", "abd", "abcd", "adc"]
"ac"

'abcdefghijklmnopqrstuvwxyz'
''
'01111111111111111111111111'
'a'
'11011111111111111111111111'
'b-z'
'22122222222222222222222222'
'ac'
'11111111111111111111111111'
'a(b,d-z)'
'22222222222222222222222222'
''