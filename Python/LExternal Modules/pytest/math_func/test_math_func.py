import math_func
import pytest
import sys


@pytest.mark.parametrize("num1, num2, result",
                         [
                             (7, 3, 10),
                             ("Hello", " World", "Hello World"),
                             (10.5, 25.5, 36)
                         ])
# @pytest.mark.skip(reason="do not run test")
def test_add(num1, num2, result):
    print(num1, num2, result)
    assert math_func.add(num1, num2) == result


@pytest.mark.skipif(sys.version_info > (3, 5), reason="do not run test")
@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 9


@pytest.mark.strings
def test_add_strings():
    result = math_func.add("Hello", " World")
    assert result == "Hello World"
    assert type(result) is str
    assert "Heldlo" not in result


@pytest.mark.strings
def test_product_strings():
    result = math_func.product("Hello ", 3) == "Hello Hello Hello "
    result = math_func.product("Hello ")
    assert result == "Hello Hello "
    assert type(result) is str
    assert "Hello" in result
