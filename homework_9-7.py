def is_prime(func):
    def wrapper(*args):
        word = []
        a = func(*args)
        for i in range(1, a+1):
            if a % i == 0:
                word.append(i)
        if len(word) > 2:
            b = 'Составное'
        else:
            b = 'Простое'
        return b
    return wrapper

# @is_prime
def sum_three(x, y, z):
    sum_ = x + y + z
    return sum_

sum_three1 = is_prime(sum_three)
print(sum_three1)

result = sum_three(7, 11, 25)
print(result)
