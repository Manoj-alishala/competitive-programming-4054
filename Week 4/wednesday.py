# Trie: Auto-Complete / City Search / Contact Search
#
# Sample Input:
# 5
# mobile mouse moneypot monitor mousepad
# 4
# S mouse
# S monkey
# P mon
# P mou
#
# Sample Output:
# True
# False
# True
# True


class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                return False
            node = node.child[ch]
        return node.end

    def prefix(self, pref):
        node = self.root
        for ch in pref:
            if ch not in node.child:
                return False
            node = node.child[ch]
        return True


def solve():
    n = int(input())
    words = input().split()

    trie = Trie()
    for w in words:
        trie.insert(w)

    q = int(input())
    for _ in range(q):
        op, text = input().split()
        if op == "S":     # Search word
            print(trie.search(text))
        else:             # Prefix check
            print(trie.prefix(text))


if __name__ == "__main__":
    solve()


# Trie: Course Code Search / Contact Search
#
# Sample Input:
# 5
# CS101 CS102 CS201 EE101 ME105
# 4
# S CS101
# S CS301
# P CS
# P EE
#
# Sample Output:
# True
# False
# True
# True


class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                node.child[ch] = TrieNode()
            node = node.child[ch]
        node.end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.child:
                return False
            node = node.child[ch]
        return node.end

    def prefix(self, pref):
        node = self.root
        for ch in pref:
            if ch not in node.child:
                return False
            node = node.child[ch]
        return True


def solve():
    n = int(input())
    words = input().split()

    trie = Trie()
    for w in words:
        trie.insert(w)

    q = int(input())
    for _ in range(q):
        op, text = input().split()
        if op == "S":
            print(trie.search(text))
        else:
            print(trie.prefix(text))


if __name__ == "__main__":
    solve()
