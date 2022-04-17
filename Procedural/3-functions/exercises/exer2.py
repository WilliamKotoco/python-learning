# enunciado gigante, não vai caber não
def do_four(function, value):
    function(value)
    function(value)


def print_twice(spam):
    print(spam)
    print(spam)


do_four(print_twice, "teste")
