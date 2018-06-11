def hello():
    print("first")
    yield 1
    print("second")
    yield 2
    print("third")
    yield 3
    print("fourth")
    yield 4
    print("fifth")
    yield 5
hello()
p=hello()
next(p)
next(p)
next(p)
next(p)
next(p)
next(p)
next(p)
