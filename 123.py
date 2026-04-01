def foo(n):
    def boo(x):
        return x + n
    return boo

zoo = foo(100)
zoo(200)
