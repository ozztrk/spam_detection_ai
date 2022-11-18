class NaiveBayes:
    # Path: src/naivebayes.py
    def __init__(self, train_data):
        # train_data is a list of lists
        self.train = train_data
        # P(spam) and P(ham)
        self.spam_prob, self.ham_prob = self.spam_distribution(train_data)
        # Vocab size
        self.voc_size = self.vocab_size(self.train)
        # Dictionary with all words and their frequency in the spam and ham messages
        self.spam_dict, self.ham_dict = self.spam_and_ham_dict()
        # Number of words in the spam and ham messages
        self.Nspam, self.Nham = self.number_of_spam_and_ham_words()
        # Smoothing parameter
        self.smooth_param = 1
        # Number of spam and ham messages
        self.spam_dict, self.ham_dict = self.spam_and_ham_dict()

    def spam_and_ham_dict(self):
        # Create a dictionary with all words and their frequency in the spam and ham messages
        spam_dict = {}
        ham_dict = {}
        for line in self.train:
            if line[0] == 'spam':
                for word in line[1:]:
                    if word in spam_dict:
                        spam_dict[word] += 1
                    else:
                        spam_dict[word] = 1
            elif line[0] == 'ham':
                for word in line[1:]:
                    if word in ham_dict:
                        ham_dict[word] += 1
                    else:
                        ham_dict[word] = 1
            else:
                print("Error")
        return spam_dict, ham_dict

    @staticmethod
    def vocab_size(train_data):
        # Create a set of all words in the training data
        vocab = set()
        for line in train_data:
            vocab.update(line[1:])
        return len(vocab)

    @staticmethod
    def spam_distribution(data):
        # Calculate the probability of a message being spam
        spam_count = 0
        for line in data:
            if line[0] == 'spam':
                spam_count += 1
        return spam_count / len(data), 1 - (spam_count / len(data))

    def number_of_spam_and_ham_words(self):
        # Calculate the number of words in the spam and ham messages
        spam_words = 0
        ham_words = 0
        for line in self.train:
            if line[0] == 'spam':
                spam_words += len(line[1:])
            else:
                ham_words += len(line[1:])

        return spam_words, ham_words

    def probability_of_word_spam(self, word):
        # P(w|spam)
        if word in self.spam_dict.keys():
            return (self.spam_dict[word] + self.smooth_param) / (self.Nspam + self.voc_size * self.smooth_param)
        else:
            return self.smooth_param / (self.Nspam + self.voc_size * self.smooth_param)

    def probability_of_word_ham(self, word):
        # P(w|ham)
        if word in self.ham_dict.keys():
            return (self.ham_dict[word] + self.smooth_param) / (self.Nham + self.voc_size * self.smooth_param)
        else:
            return self.smooth_param / (self.Nham + self.voc_size * self.smooth_param)

    def classify(self, message):
        prob_given_message_is_spam = self.spam_prob
        prob_given_message_is_ham = self.ham_prob
        for word in message:
            prob_given_message_is_spam *= self.probability_of_word_spam(word)
            prob_given_message_is_ham *= self.probability_of_word_ham(word)
        if prob_given_message_is_ham > prob_given_message_is_spam:
            return 'not spam'
        elif prob_given_message_is_ham < prob_given_message_is_spam:
            return 'spam'
        else:
            return 'equal probability'
