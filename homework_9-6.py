def all_variants(text):
    n = len(text)
    for j in range(1, n+1):
        for x in range(n):
            y = x + j
            if y < n+1:
                yield text[x:y]
                y += 1
                x += 1


a = all_variants("abc")
for i in a:
    print(i)