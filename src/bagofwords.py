from collections import Counter
import re


class BagOfWords:
    # Similar to CountVectorizer in Scikit-Learn?
    def __init__(self, corpus_messages: list):
        self.corpus = corpus_messages

    def lower_text(self):
        lower_text = [line.lower() for line in self.corpus]
        return lower_text

    def remove_punctuation(self):
        lower_text = [re.sub('[+\-/(){}\[\]<>!§üäö£$%&=^\'?@*#€¿_\",.:;0-9]', '', line) for line in self.corpus]
        correction = [line.replace("\x92", '\'') for line in lower_text]
        return correction

    def tokenize_text(self) -> list:
        return [line.split() for line in self.corpus]

    def count_frequencies(self):
        # Count the frequencies of the words in the corpus
        # Umformen in Binär (0, 1) anstatt Häufigkeit?
        word_counts = [Counter(line) for line in self.corpus]
        return word_counts

    def prep_corpus(self):
        self.corpus = self.lower_text()
        self.corpus = self.remove_punctuation()
        self.corpus = self.tokenize_text()
        return self.corpus
