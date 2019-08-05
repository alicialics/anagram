import collections

class Dictionary:
    def __init__(self, words):
        self.root = Node() 
        for word in words:
            self.root.add_word(word, self.get_word_frequency_table(word))

    def match_anagram(self, input):
        return self.root.match_anagram(self.get_word_frequency_table(input))

    def get_word_frequency_table(self, word):
        return collections.Counter(sorted(word.lower()))

class Node:
    def __init__(self):
        self.words = []
        self.children_map = {}

    def add_word(self, word, frequency_table):
        # We've processed every letter in the frequency_table,
        # just add the word to the list of words.
        if not frequency_table:
            self.words.append(word)
            return
        
        # Gets the next character + frequency and recursively insert into a child bucket.
        letter = next(iter(frequency_table))
        frequency = frequency_table.pop(letter)
        self.get_child(letter, frequency).add_word(word, frequency_table)

    def get_child(self, letter, frequency):
        pair = (letter, frequency)
        # Creates a new child from letter + frequency if it doesn't exist.
        if not pair in self.children_map:
            self.children_map[pair] = Node()
        return self.children_map[pair]

    def match_anagram(self, frequency_table):
        # Reached the leaf of the tree.
        if len(frequency_table) == 0 or len(self.children_map) == 0:
            return self.words
        
        # Find each match child and recursively match.
        words = self.words.copy()
        for pair in self.children_map:
            if pair[1] <= frequency_table.get(pair[0], 0):
                new_frequency_table = frequency_table.copy()
                del new_frequency_table[pair[0]]
                words += self.children_map[pair].match_anagram(new_frequency_table)

        return words


class SlowDictionary:
    def __init__(self, words):
        self.words = words

    def match_anagram(self, input):
        # Just go through each word in dictionary and perform a match.
        frequency_table = collections.Counter(input.lower())
        matches = []
        for word in self.words:
            new_frequency_table = frequency_table.copy()
            found = True
            for letter in word.lower():
                if new_frequency_table.get(letter, 0) == 0:
                    found = False
                    break
                new_frequency_table[letter] = new_frequency_table.get(letter, 0) - 1
                
            if found:
                matches.append(word)
        return matches
