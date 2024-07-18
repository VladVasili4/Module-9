import io
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file = open(file_name, 'a', encoding='UTF-8')
        for data_ in data_set:
            file.write(str(data_) + '\n')
        return file
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 'Это конец')

class  MysticBall:
    def __init__(self, words):
        self.words = words

    def __call__(self, *args):
        self.choice = choice(self.words)
        return self.choice


first_ball = MysticBall(['Это строчка', 'А', 'это', 'уже', 'число', '5', 'в', 'списке', 'Это конец'])
print(first_ball())
print(first_ball())
print(first_ball())






