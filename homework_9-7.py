def is_prime(func):
    def wrapper(*args):
        word = []
        a = func(*args)
        for i in range(1, a+1):
            if a % i == 0:
                word.append(i)
        if len(word) > 2:
            b = f'Составное\n{a}'
        else:
            b = f'Простое\n{a}'
        return b
    return wrapper

@is_prime
def sum_three(x, y, z):
    sum_ = x + y + z
    return sum_


result = sum_three(7, 11, 25)
print(result)
