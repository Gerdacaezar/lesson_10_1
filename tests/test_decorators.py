import pytest

from src.decorators import log


@log()
def func_test(x, y):
    return x + y


def test_log_decorator_correct_func(capsys):
    func_test(1, 2)
    assert capsys.readouterr().out == "func_test ok\n"


def test_log_decorator_incorrect_func(capsys):
    with pytest.raises(TypeError):
        func_test(1, "2")
        assert (
            capsys.readouterr().out
            == "func_test error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}\n"
        )


@log(filename="mylog.txt")
def func_test_with_params(x, y):
    return x + y


def test_log_decorator_correct_save_file():
    func_test_with_params(1, 2)
    with open("mylog.txt", "r") as file:
        assert file.read() == "func_test_with_params ok"


def test_log_decorator_incorrect_save_file():
    with pytest.raises(TypeError):
        func_test_with_params(1, "2")
        with open("mylog.txt", "r") as file:
            assert (
                file.read()
                == """
func_test_with_params error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'), {}
"""
            )
