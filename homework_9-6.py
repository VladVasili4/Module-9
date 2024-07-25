def all_variants(text):
    n = len(text)
    y = 1
    for x in range(n):
        yield text[x]
        x += 1
    y += 1
    for x in range(n):
        if y < n + 1:
            yield text[x:y]
            x += 1
            y += 1
    y = 3
    for x in range(n):
        if y < n + 1:
            yield text[x:y]
            x += 1
            y += 1


a = all_variants("abc")
for i in a:
    print(i)