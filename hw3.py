class CountVectorizer:
    """
    мой мини CountVectorizer, преобразует текст в матрицу подсчёта слов
    """
    def __init__(self):
        self.vocab = []

    def fit_transform(self, data):
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


def test_count_vectorizer():
    """
    я не знаю что такое проверка, вот держи глупую функцию
    """
    vectorizer = CountVectorizer()
    corpus = ["жила была свынюшка по имени пигмалион",
              "свынюшка жила очень очень счастливо",
              "свынюшка пигмалион ОЧЕНЬ любила спа",
              "валяться в грязи - роскошно"]

    matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()
    print("словечки: ", feature_names)
    print("матричка: ", matrix)

if __name__ == "__main__":
    test_count_vectorizer()