from random import uniform


class Generate:
    def __init__(self, model):
        self.model = model

    def generate_text(self):
        text = ''
        default1 = '^'
        while 1:
            default1 = self.get_rand_word1(self.model[default1])
            if default1 == '^':
                break

            if default1 == '.' or default1 == '!' or default1 == '?':
                text += default1
                break

            if default1:
                text += ' ' + default1
            else:
                default1 = '^'
        return text

    @staticmethod
    def get_rand_word(model):
        m_word = ''
        sum_of_w, sum_of_w2 = 0, 0
        for word, w in model:
            sum_of_w += w
        random = uniform(0, sum_of_w)
        for word, w in model:
            sum_of_w2 += w
            if random < sum_of_w2:
                m_word = word
                break
        return m_word

    @staticmethod
    def get_rand_word2(model):
        word = ''
        sum_of_w, w = 0.0, 0.0
        for key in model:
            sum_of_w += model.get(key, 0.0)
        random = uniform(0, sum_of_w)
        for key in model:
            w += model.get(key, 0.0)
            if random < w:
                word = key
                break
        return word

    def get_text_from_second_model(self):
        text = ''
        default = '^'
        while 1:
            default = self.get_rand_word2(self.model[default])
            if default == '.' or default == '!' or default == '?':
                text += default
                break
            if default == '^':
                break
            if default:
                text += ' ' + default
            else:
                default = '^'

        return text
