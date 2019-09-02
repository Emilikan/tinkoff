from Train import Train
from Generate import Generate

# создаем и обучаем модель
model = Train('src/cheys.txt').auto_refactoring_for_bigrams()
# выводим текст
for i in range(5):
    text = Generate(model).get_text_from_second_model()
    print(text)
