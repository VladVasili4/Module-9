def all_variants(text):
    i = '0'
    while i in text:
        yield i
        i += 1



a = all_variants("abc")
for i in a:
    print(i)

print(a)