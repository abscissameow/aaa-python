import numpy as np


class CountVectorizer:
    """
    мой мини CountVectorizer, преобразует текст в матрицу подсчёта слов
    """
    def __init__(self):
        self.vocab = []

    def fit_transform(self, data):
        self.vocab = []
        if not isinstance(data, list):
            raise TypeError("дай список предложений пожалуйста")

        word_counts = []
        for sentence in data:
            sentence = sentence.lower()
            words = sentence.split()

            word_count = {}
            for word in words:
                if word not in self.vocab:
                    self.vocab.append(word)
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            word_counts.append(word_count)

        matrix = []
        for word_count in word_counts:
            row = [word_count.get(key, 0) for key in self.vocab]
            matrix.append(row)
        return matrix

    def get_feature_names(self):
        return self.vocab


class TfidfTransformer:
    """
    превращает матрицу количества слов в матрицу TF-IDF
    """
    def __init__(self):
        self.tfidfs = []

    def tf(self, matrix):
        tf_matrix = []
        for row in matrix:
            total_words = sum(row)
            tfs = [count/total_words if total_words else 0 for count in row]
            tf_matrix.append(tfs)
        return tf_matrix

    def idf(self, matrix):
        docs_count = len(matrix)
        docs_with_word = np.count_nonzero(matrix, axis=0)
        idfs = [
            np.log((docs_count+1) / (word_docs+1)) + 1
            for word_docs in docs_with_word
            ]
        return idfs

    def fit_transform(self, matrix):
        tfs = self.tf(matrix)
        idfs = self.idf(matrix)
        for tf_row in tfs:
            self.tfidfs.append(
                [round(tf*idf, 3) for tf, idf in zip(tf_row, idfs)]
                )
        return self.tfidfs


class TfidfVectorizer(CountVectorizer):
    """
    объединяет в себе усилия двух классов - CountVectorizer и TfidfTransformer
    """

    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        tfidf_matrix = self.transformer.fit_transform(count_matrix)
        return tfidf_matrix


if __name__ == "__main__":
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(X)
