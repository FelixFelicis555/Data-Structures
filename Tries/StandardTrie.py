from simpleprefixtree import SimpleTrieNode


class TrieNode(SimpleTrieNode):
    def __init__(self, value=None):
        super().__init__(value)
        self.is_word = False


class StandardTrie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        temp = self.root
        for c in word.lower():
            val = ord(c) - 97
            if not temp.children[val]:
                node = TrieNode(c)
                temp.children[val] = node
            temp = temp.children[val]
        temp.is_word = True

    def is_word_present(self, word):
        temp = self.root
        for c in word.lower():
            val = ord(c) - 97
            if not temp.children[val]:
                return False
            temp = temp.children[val]
        return temp.is_word


def main():
    trie = StandardTrie()
    trie.add('hello')
    trie.add('great')
    trie.add('hell')
    trie.add('to')
    trie.add('yo')
    trie.add('cruel')
    trie.add('today')
    trie.add('until')
    trie.add('zero')

    print(trie.is_word_present(input('Please enter a word to search: ')))


if __name__ == '__main__':
    main()