first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(i[0]) - len(i[1]) for i in zip(first, second) if len(i[0]) != len(i[1]))
print(list(first_result))

second_result = (len(x) == len(y) for x in first for y in second if first.index(x) == second.index(y))
print(list(second_result))

