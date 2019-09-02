import re
from collections import defaultdict


# функция для тестирования кода во время написания (использовать только при написании)
def test(a):
    lines = Train('src/cheys.txt').get_file('src/cheys.txt')
    words = Train('src/cheys.txt').get_words(lines)
    bigrams = Train('src/cheys.txt').get_bigrams(words)
    model = Train('src/cheys.txt').create(bigrams)
    if a == 1:
        for i in bigrams:
            print(i)
    if a == 2:
        print(model)


class Train:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lines = self.get_file(file_path)
        self.words = self.get_words(self.lines)
        self.bigrams = self.get_bigrams(self.words)

    def get_model(self):
        return self.create(self.bigrams)

    r_compile = re.compile(u'[а-яА-Я]+|[.!?,]+')

    @staticmethod
    def get_default_w(bigrams):
        default_w = 0.0
        for _ in bigrams:
            default_w += 1
        return default_w

    def auto_refactoring_for_bigrams(self):
        m_dict = {}

        default_w = self.get_default_w(self.bigrams)

        lines = self.get_file(self.file_path)
        words = self.get_words(lines)
        bigrams = self.get_bigrams(words)

        for bigram in bigrams:
            new_dict = {}
            if m_dict.get(bigram[0], 0) == 0:
                # если элемента нет, то мы добавлям элемент
                w = 1/default_w
                new_dict[bigram[1]] = w
                m_dict[bigram[0]] = new_dict
            else:
                # если элемент есть, то у нас 2 случая
                old_dict = m_dict[bigram[0]]
                if old_dict.get(bigram[1], 0) == 0:
                    # если мы добавляем новое связное слово
                    w = 1/default_w
                    old_dict[bigram[1]] = w
                    m_dict[bigram[0]] = old_dict
                else:
                    # если мы добавляем старое следующее слово, то считаем новую вероятность выпадения
                    w = 1/default_w + old_dict[bigram[1]]
                    old_dict[bigram[1]] = w
                    m_dict[bigram[0]] = old_dict

        return m_dict

    @staticmethod
    def create(bigrams):
        one, two = defaultdict(lambda: 0), defaultdict(lambda: 0)
        for default1, default2 in bigrams:
            one[default1] += 1
            two[default1, default2] += 1
        model = {}
        for (default1, default2), w in two.items():
            if default1 in model:
                model[default1].append((default2, w / one[default1]))
            elif one[default1, default2] != 0:
                model[default1] = [(default2, w / one[default1, default2])]
            else:
                model[default1] = [(default2, 0)]
        return model

    @staticmethod
    def get_bigrams(words):
        # знак '^' - начало предложения
        default1 = '^'
        # разделяем текст на связки по 2 слова. Разделяем и предложения
        for default2 in words:
            yield default1, default2
            if default2 == '.' or default2 == '!' or default2 == '?':
                default1 = '^'
            else:
                default1 = default2

    def get_words(self, lines):
        # получаем слова
        for line in lines:
            for word in self.r_compile.findall(line):
                yield word

    @staticmethod
    def get_file(file_path):
        # открываем файл
        file = open(file_path)
        # нижний регистр
        for line in file:
            yield line.lower()


test(1)
