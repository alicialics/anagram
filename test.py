import unittest
from dictionary import Dictionary, SlowDictionary
import collections
import time

class MyTests(unittest.TestCase):    
    def test_words(self):
        print("Ingesting words from words.txt...")
        with open("words.txt", 'r') as file:
            words = [word.strip() for word in file.readlines()]
    
        dictionary = Dictionary(words)
        slow_dictionary = SlowDictionary(words)

        for input_str in ["beautiful", "funnyordie", "zyzyzyzy", "abc", "abcdefghijklmnopqrstuvwxyz"*10]:
            print("Testing word %s" % input_str)
            actual_start = time.time()
            actual = collections.Counter(dictionary.match_anagram(input_str))
            actual_end = time.time()
            print("Time elapsed:", actual_end - actual_start)
            expected = collections.Counter(slow_dictionary.match_anagram(input_str))
            print("Naive method time elapsed:", time.time() - actual_end)
            self.assertEqual(actual, expected)
            
             
if __name__ == '__main__':
    unittest.main()
