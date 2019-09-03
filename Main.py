from Train import Train
from Generate import Generate
import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-file_path', '--file_path', default='src/cheys.txt')
    parser.add_argument('-model', '--model', default='bigrams')

    return parser


if __name__ == '__main__':
    parser = create_parser()
    arg = parser.parse_args(sys.argv[1:])
    print(arg)
    if arg.model == 'bigrams':
        model = Train(arg.file_path).get_model()
        for i in range(5):
            text = Generate(model).generate_text()
            print(text)
    elif arg.model == 'probabilistic_model':
        # создаем и обучаем модель
        model = Train('src/cheys.txt').auto_refactoring_for_bigrams()
        # выводим текст
        for i in range(5):
            text = Generate(model).get_text_from_second_model()
            print(text)
    else:
        print('ошибка')
