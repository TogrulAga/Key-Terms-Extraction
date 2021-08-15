import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from lxml import etree
from string import punctuation
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


class KeyTermExtractor:
    def __init__(self):
        self.xml = None
        self.tokenized_news = []
        self.tfidf_matrix = None
        self.vocabulary = None
        self.counts_dict = dict()
        self.lemmatizer = WordNetLemmatizer()
        self.get_news()
        self.find_most_frequent_words()
        self.print_most_frequent_words()

    def get_news(self):
        self.xml = etree.parse("news.xml").getroot()

    def find_most_frequent_words(self):
        stop_words = stopwords.words('english')
        for news in self.xml[0]:
            tokenized_news = word_tokenize(news[1].text.lower())
            tokenized_news = list(map(lambda x: self.lemmatizer.lemmatize(x, "n"), tokenized_news))
            tokenized_news = list(filter(lambda x: x not in stop_words and x not in punctuation, tokenized_news))
            tokenized_news = list(map(lambda x: nltk.pos_tag([x]), tokenized_news))
            tokenized_news = list(filter(lambda x: x[0][1] == "NN", tokenized_news))
            tokenized_news = list(map(lambda x: x[0][0], tokenized_news))
            self.tokenized_news.append(tokenized_news)

        self.calculate_tf_idf()
        for n, news in enumerate(self.xml[0]):
            self.counts_dict[news[0].text] = list(zip(self.vocabulary[(-self.tfidf_matrix[n]).argsort()[:10]].tolist(), self.tfidf_matrix[n][(-self.tfidf_matrix[n]).argsort()[:10]].tolist()))
            self.counts_dict[news[0].text] = sorted(self.counts_dict[news[0].text], key=lambda x: (x[1], x[0]), reverse=True)[:5]

    def calculate_tf_idf(self):
        news = [" ".join(news) for news in self.tokenized_news]
        vectorizer = TfidfVectorizer()
        self.tfidf_matrix = vectorizer.fit_transform(news).toarray()
        self.vocabulary = np.asarray(vectorizer.get_feature_names())

    def print_most_frequent_words(self):
        for title, words in self.counts_dict.items():
            print(f"{title}:")
            print(*list(map(lambda x: x[0], words)))
            print()


if __name__ == "__main__":
    _ = KeyTermExtractor()
