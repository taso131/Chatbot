class Vocabulary:
    PAD_TOKEN = 0  # padding short sentences
    SOS_TOKEN = 1  # start of sentence
    EOS_TOKEN = 2  # end of sentence

    def __init__(self, name):
        self.name = name
        self.word2index = {}
        self.word2count = {}
        self.index2word = {self.PAD_TOKEN: "PAD",
                           self.SOS_TOKEN: "SOS", self.EOS_TOKEN: "EOS"}
        self.num_words = 3
        self.num_sentences = 0
        self.longest_sentence = 0

    def update(self, tokens):
        sentence_len = 0
        for word in tokens:
            sentence_len += 1
            self.add_word(word)
        if sentence_len > self.longest_sentence:
            self.longest_sentence = sentence_len
        self.num_sentences += 1

    def add_word(self, word):
        if word not in self.word2index:
            self.word2index[word] = self.num_words
            self.word2count[word] = 1
            self.index2word[self.num_words] = word
            self.num_words += 1
        else:
            self.word2count[word] += 1
