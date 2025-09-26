def build(x, y):
    return lambda: x * x + y * y

f = build(1,2)

print(f)

print(f())