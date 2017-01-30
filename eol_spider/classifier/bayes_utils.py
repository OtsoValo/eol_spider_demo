import numpy
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.naive_bayes import MultinomialNB


class BayesUtils(object):

    @staticmethod
    def input_data(dataset):
        train_words = []
        train_tags = []
        test_words = []
        test_tags = []
        for train_doc in dataset.train_docs:
            train_words.append(train_doc[1])
            train_tags.append(train_doc[0])
        for test_doc in dataset.test_docs:
            test_words.append(test_doc[1])
            test_tags.append(test_doc[0])

        return train_words, train_tags, test_words, test_tags

    # TfidfVectorizer
    # def __init__(self, input='content', encoding='utf-8',
    #              decode_error='strict', strip_accents=None, lowercase=True,
    #              preprocessor=None, tokenizer=None, analyzer='word',
    #              stop_words=None, token_pattern=r"(?u)\b\w\w+\b",
    #              ngram_range=(1, 1), max_df=1.0, min_df=1,
    #              max_features=None, vocabulary=None, binary=False,
    #              dtype=np.int64, norm='l2', use_idf=True, smooth_idf=True,
    #              sublinear_tf=False):
    # X = vectorizer.fit_transform(corpus)
    # idf = vectorizer.idf_
    # print dict(zip(vectorizer.get_feature_names(), idf))
    @staticmethod
    def vectorize(train_words, test_words):
        v = TfidfVectorizer(lowercase=True, analyzer='word', max_df=1.0, min_df=1)
        # v = CountVectorizer(lowercase=True, analyzer='word', max_df=1.0, min_df=1)
        # v = HashingVectorizer(lowercase=True, n_features=30000, non_negative=True)
        train_data = v.fit_transform(train_words)
        test_data = v.transform(test_words)
        return train_data, test_data, v

    @staticmethod
    def evaluate(actual, pred):
        m_precision = metrics.precision_score(actual, pred, average=None)
        m_recall = metrics.recall_score(actual, pred, average=None)
        return m_precision, m_recall

    @staticmethod
    def train_clf(train_data, train_tags):
        clf = MultinomialNB(alpha=0.01)
        clf.fit(train_data, numpy.asarray(train_tags))
        return clf

    @staticmethod
    def vectorize_unknown(unknown_words, vectorizer):
        analyzer = vectorizer.build_analyzer()
        analyzer_result = analyzer(unknown_words[0])
        unknown_data = vectorizer.transform(unknown_words)
        # print unknown_words
        # print unknown_data
        # print analyzer_result
        return unknown_data, analyzer_result

