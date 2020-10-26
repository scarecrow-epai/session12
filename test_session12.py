import re
import os
import math
import pytest
import inspect
import session12
import datetime
import calculator.sin, calculator.cos, calculator.tan, calculator.sigmoid, calculator.relu, calculator.softmax, calculator.log, calculator.exp

README_CONTENT_CHECK_FOR = [
    "sin",
    "cos",
    "tan",
    "sigmoid",
    "relu",
    "tanh",
    "softmax",
    "log",
    "exp",
]


def test_readme_exists():
    """
    Test funtion to check if README exists.
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test if README contains atleast 200 words.
    """
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 100
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    """
    Check if README contains required functions..
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass

    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    """
    Test function to check README file formatting.
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """
    Returns pass if used four spaces for each level of syntactically \
    significant indenting.
    """
    lines = inspect.getsource(session12)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    """
    Test function to check if any function names have any capital letters.
    """
    functions = inspect.getmembers(session12, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_sin():
    """
    Test for sin function.
    """
    assert calculator.sin.calc_sin(10) == math.sin(10)


def test_cos():
    """
    Test for cos function.
    """
    assert calculator.cos.calc_cos(10) == math.cos(10)


def test_tan():
    """
    Test for tan function.
    """
    assert calculator.tan.calc_tan(10) == math.tan(10)


def test_sigmoid():
    """
    Test for sigmoid function.
    """
    assert calculator.sigmoid.calc_sigmoid(0.7) == 0.6681877721681662


def test_relu():
    """
    Test for relu function.
    """
    assert calculator.relu.calc_relu(0.7) == 0.7


def test_tanh():
    """
    Test for tanh function.
    """
    assert calculator.tanh.calc_tanh(0.7) == 0.6043677771171636


def test_softmax():
    """
    Test for softmax function.
    """
    assert calculator.softmax.calc_softmax([1, 2, 3]) == [
        0.09003057317038046,
        0.24472847105479767,
        0.6652409557748219,
    ]


def test_log():
    """
    Test for log function.
    """
    assert calculator.log.calc_log(10) == math.log(10)


def test_exp():
    """
    Test for exp function.
    """
    assert calculator.exp.calc_exp(10) == math.exp(10)


def test_d_sin():
    """
    Test for dsin function.
    """
    assert calculator.sin.calc_d_sin(-0.5440211108893698) == 0.8556343548213666


def test_d_cos():
    """
    Test for dcos function.
    """
    assert calculator.cos.calc_d_cos(-0.8390715290764524) == 0.7440230792707043


def test_d_tan():
    """
    Test for dtan function.
    """
    assert calculator.tan.calc_d_tan(0.6483608274590866) == 1.5739898037260205


def test_d_sigmoid():
    """
    Test for dsigmoid function.
    """
    assert calculator.sigmoid.calc_d_sigmoid(0.6681877721681662) == 0.22404767527442665


def test_d_relu():
    """
    Test for drelu function.
    """
    assert calculator.relu.calc_d_relu(0.7) == 1


def test_d_tanh():
    """
    Test for dtanh function.
    """
    assert calculator.tanh.calc_d_tanh(0.6043677771171636) == 0.7082376675077355


def test_d_softmax():
    """
    Test for dsoftmax function.
    """
    assert calculator.softmax.calc_d_softmax(
        [0.09003057317038046, 0.24472847105479767, 0.6652409557748219]
    ) == [0.1892365926720373, 0.2083469224026804, 0.24755896848347855]


def test_d_log():
    """
    Test for dlog function.
    """
    assert calculator.log.calc_d_log(2.302585092994046) == 0.43429448190325176


def test_d_exp():
    """
    Test for dexp function.
    """
    assert calculator.exp.calc_d_exp(10) == math.exp(10)
