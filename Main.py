from Train import Train
from Generate import Generate

# создаем и обучаем модель
model = Train('src/cheys.txt').get_model()
# выводим текст
for i in range(5):
    text = Generate(model).generate_text()
    print(text)
