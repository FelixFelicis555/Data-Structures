class SimpleTrieNode:
    def __init__(self, value=None):
        self.value = value
        self.children = [None for _ in range(26)]


class SimpleTrie:
    def __init__(self):
        self.root = SimpleTrieNode()

    def add(self, word):
        temp = self.root
        for c in word.lower():
            val = ord(c) - 97
            if not temp.children[val]:
                node = SimpleTrieNode(c)
                temp.children[val] = node
            temp = temp.children[val]

    def is_word_present(self, word):
        temp = self.root
        for c in word.lower():
            val = ord(c) - 97
            if not temp.children[val]:
                return False
            temp = temp.children[val]

        return True


def main():
    trie = SimpleTrie()
    trie.add('hello')
    trie.add('great')
    trie.add('amazing')
    trie.add('true')
    trie.add('yo')
    trie.add('cruel')
    trie.add('today')
    trie.add('until')
    trie.add('zero')

    print(trie.is_word_present(input('Please enter a word to search: ')))


if __name__ == '__main__':
    main()