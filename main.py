import re
from dictionary import Dictionary
import sys

def main():
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3+")

    words = []
    print("Ingesting words from words.txt...")
    with open("words.txt", 'r') as file:
        words = [word.strip() for word in file.readlines()]
    
    dictionary = Dictionary(words)

    while True:
        print("Please enter letters you want to use:")
        letters = input()
        if not re.match("^[A-za-z]+$", letters):
            print("%s is considered invalid input, please only use english alphabets a-z." % letters)
            continue

        matches = dictionary.match_anagram(letters)
        print("")
        for word in sorted(matches):
            print(word)
        
        print("Found %d matches." % len(matches))    
        


if __name__ == '__main__':
    main()
