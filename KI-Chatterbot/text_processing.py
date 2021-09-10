import pandas as pd
import numpy as np
import re
import string
import json
import joblib
import vocabulary
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from tens


class Text_Processor():

    def __init__(self) -> None:
        self.data = self.read_data()
        self.lemmatizer = WordNetLemmatizer()
        self.vocab = vocabulary('Data_vocab')

    def read_data():
        with open('Intents.json', 'r') as file:
            return json.load(file)

    def json_to_pd_data_frame(self, feat_1, feat_2, is_pattern):
        is_pattern = is_pattern
        df = pd.DataFrame(columns=[feat_1, feat_2])
        for intent in self.data['intents']:
            if is_pattern:
                for pattern in intent['patterns']:
                    w = pattern
                    df_to_append = pd.Series(
                        [w, intent['tag']], index=df.columns)
                    df = df.append(df_to_append, ignore_index=True)
            else:
                for response in intent['responses']:
                    w = response
                    df_to_append = pd.Series(
                        [w, intent['tag']], index=df.columns)
                    df = df.append(df_to_append, ignore_index=True)
        return df

    def tokenizer(self, entry):
        tokens = entry.split()
        re_punc = re.compile('[%s]' % re.escape(string.punctuation))
        tokens = [re_punc.sub('', w) for w in tokens]
        tokens = [word for word in tokens if word.isalpha()]
        tokens = [self.lemmatizer.lemmatize(w.lower()) for w in tokens]
        stop_words = set(stopwords.words('english'))
        tokens = [w for w in tokens if not w in stop_words]
        tokens = [word.lower() for word in tokens if len(word) > 1]
        return tokens

    def remove_stop_words(tokenizer, df, feature):
        doc_without_stopwords = []
        for entry in df[feature]:
            tokens = tokenizer(entry)
            joblib.dump(tokens, 'tokens.pkl')
            doc_without_stopwords.append(' '.join(tokens))
        df[feature] = doc_without_stopwords
        return

    def create_vocab(self, tokenizer, df, feature):
        for entry in df[feature]:
            tokens = tokenizer(entry)
            self.vocab.update(tokens)
        joblib.dump(self.vocab, 'vocab.pkl')
        return

    def encoder(df, feature):
        t =
