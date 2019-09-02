class Generate:
    def __init__(self, model):
        self.model = model

    def generate_text(self):
        phrase = ''
        default1 = '^'
        while 1:
            default1 = self.get_rand_word(self.model[default1])
            if default1 == '^':
                break

            if default1 == '.' or default1 == '!' or default1 == '?':
                phrase += default1
                break

            if default1:
                phrase += ' ' + default1
            else:
                default1 = '^'
        return phrase

    @staticmethod
    def get_rand_word(model):
        sum_of_w = 0
        for word, w in model:
            sum_of_w = w
        for word, w in model:
            if w == sum_of_w:
                return word
