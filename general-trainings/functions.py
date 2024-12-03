def v(a: object) -> object:
    print(a)


v("Name")


def sum_nums(a, b):
    """
      The doc...
    @param a:numeric
    @param b:numeric
    @return:numeric
    """
    return a + b


v(sum_nums(1, 5))
