def checking_that_arg_is(predicate, error_message):
    def wrapper(func):
        def inner(arg):
            if not predicate(arg):
                raise ValueError(error_message)
            return func(arg)

        return inner

    return wrapper


@checking_that_arg_is(lambda x: x > 0, "Value must be greater than 0!")
def example_function(value):
    return value * 2


print(example_function(5))  # >>> 10


def greater_than(value):
    def predicate(arg):
        return arg > value

    return predicate


def in_(*values):
    def predicate(arg):
        return arg in values

    return predicate


def not_(other_predicate):
    def predicate(arg):
        return not other_predicate(arg)

    return predicate


@checking_that_arg_is(greater_than(0), "Non-positive!")
@checking_that_arg_is(not_(in_(5, 15, 42)), "Bad value!")
def foo(arg):
    return arg


print(foo(4))
