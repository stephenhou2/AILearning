def count():
    fs = []

    for i in range(1, 4):
        def f(i):
            def g():
                print(i*i)
            return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

f1()
f2()
f3()

