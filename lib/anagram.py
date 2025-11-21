class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        sorted_word = sorted(self.word)
        matches = []
        for w in words:
            if sorted(w.lower()) == sorted_word:
                matches.append(w)
        return matches
