# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, possible_anagrams):
        matches = []
        for anagram in possible_anagrams:
            if anagram.lower() != self.word and ''.join(sorted(anagram.lower())) == self.sorted_word:
                matches.append(anagram)
        return matches