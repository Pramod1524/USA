def outer(func):
    def inner():
        print('*' * 2)
        func()
        print('@' * 2)

    return inner()
@outer
def f1():
    print('hello')
