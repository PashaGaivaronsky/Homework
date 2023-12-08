def debug(func):
    def wrap(*args):
        return f"name functoin:'{func.__name__}',arguments function:'{args}',result function:'{func()}'"
    return wrap

@debug
def hello(*args):
    return "Hello World"


print(hello(23, 11))
