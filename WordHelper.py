import os

class WordHelper:
    def __init__(self):
        self.wordlists = {}
        self._import_words()

    def _parse_words(self, file_path):
        with open(file_path, 'r') as f:
            for line in f.readlines():
                for word in line.strip().split():
                    if len(word) in self.wordlists:
                        self.wordlists.get(len(word)).add(word.lower())
                    else:
                        self.wordlists[len(word)] = {word.lower()}

    def _import_words(self):
        for _, _, files in os.walk('WordLists'):
            for file in files:
                self._parse_words(f"WordLists/{file}")

    def _matches_pattern(self, word, pattern):
        if len(word) != len(pattern):
            return False

        for char in range(len(word)):
            if pattern[char] != '_' and pattern[char] != word[char]:
                return False

        return True

    def parse(self, parse_pattern):
        tmp_set = set()
        for word in self.wordlists[len(parse_pattern)]:
            if self._matches_pattern(word, parse_pattern):
                tmp_set.add(word)

        return tmp_set