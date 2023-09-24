import basicMath
import pytest

# add
def test_add_when_positive_integer_given():
    assert basicMath.add(3, 4) == 7

def test_add_when_negative_integer_given():
    assert basicMath.add(-3, -5) == -8
    
def test_add_when_one_negative_integer():
    assert basicMath.add(-3, 5) == 2

def test_add_when_string_given():
    assert basicMath.add("Hi ", "test") == "Hi test"


def test_add_when_one_string_given():
    with pytest.raises(Exception):
        basicMath.add("Hi ", 1)

def test_add_when_float_given():
    assert basicMath.add(2.3, 5.3) == 7.6

def test_add_when_one_float_given():
    assert basicMath.add(2.3, 5) == 7.3

def test_add_when_negative_float_given():
    assert basicMath.add(2, -2.5) == -0.5

def test_add_when_complex():
    assert basicMath.add((3 + 4j), (2 - 1j)) == (5 + 3j)

def test_add_when_boolean_true_false():
    assert basicMath.add(True, False) == 1
    
def test_add_when_boolean_true_true():
    assert basicMath.add(True, True) == 2
    
def test_add_when_boolean_false_false():
    assert basicMath.add(False, False) == 0

def test_add_when_lists_given():
    x = ["apple", "banana"]
    y = ["cherry"]
    assert basicMath.add(x, y) == ["apple", "banana", "cherry"]

def test_add_when_list_given_and_int():
    x = ["apple", "banana"]
    y = 1
    with pytest.raises(Exception):
        basicMath.add(x, y)

def test_add_when_given_zeros():
    assert basicMath.add(0, 0) == 0

def test_add_when_first_number_is_zero():
    assert basicMath.add(0, 2) == 2

def test_add_when_second_numer_is_zero():
    assert basicMath.add(2, 0) == 2

# subtract
def test_subtract_when_positive_integer_given():
    assert basicMath.subtract(3, 4) == -1

def test_subtract_when_negative_integer_given():
    assert basicMath.subtract(-3, -5) == 2
    
def test_subtract_when_one_negative_integer():
    assert basicMath.subtract(-3, 5) == -8

def test_subtract_when_string_given():
    with pytest.raises(Exception):
        basicMath.subtract("Hi ", "test")

def test_subtract_when_one_string_given():
    with pytest.raises(Exception):
        basicMath.subtract("Hi ", 1)

def test_subtract_when_float_given():
    assert basicMath.subtract(2.3, 5.3) == -3

def test_subtract_when_one_float_given():
    assert basicMath.subtract(2.3, 5) == -2.7

def test_subtract_when_negative_float_given():
    assert basicMath.subtract(2, -2.5) == 4.5

def test_subtract_when_complex():
    assert basicMath.subtract((3 + 4j), (2 - 1j)) == (1 + 5j)

def test_subtract_when_boolean_true_false():
    assert basicMath.subtract(True, False) == 1
    
def test_subtract_when_boolean_true_true():
    assert basicMath.subtract(True, True) == 0
    
def test_subtract_when_boolean_false_false():
    assert basicMath.subtract(False, False) == 0

def test_subtract_when_lists_given():
    x = ["apple", "banana"]
    y = ["cherry"]
    with pytest.raises(Exception):
        basicMath.subtract(x, y)

def test_subtract_when_list_given_and_int():
    x = ["apple", "banana"]
    y = 1
    with pytest.raises(Exception):
        basicMath.subtract(x, y)

def test_subtract_when_given_zeros():
    assert basicMath.subtract(0, 0) == 0

def test_subtract_when_first_number_is_zero():
    assert basicMath.subtract(0, 2) == -2

def test_subtract_when_second_numer_is_zero():
    assert basicMath.subtract(2, 0) == 2

# multiply
def test_multiply_when_positive_integer_given():
    assert basicMath.multiply(3, 4) == 12

def test_multiply_when_negative_integer_given():
    assert basicMath.multiply(-3, -5) == 15
    
def test_multiply_when_one_negative_integer():
    assert basicMath.multiply(-3, 5) == -15

def test_multiply_when_string_given():
    with pytest.raises(Exception):
        basicMath.multiply("Hi ", "test")

def test_multiply_when_one_string_given():
    assert basicMath.multiply("Hi ", 1) == "Hi "

def test_multiply_when_float_given():
    assert basicMath.multiply(2.3, 5.3) == 12.19

def test_multiply_when_one_float_given():
    assert basicMath.multiply(2.3, 5) == 11.5

def test_multiply_when_negative_float_given():
    assert basicMath.multiply(2, -2.5) == -5

def test_multiply_when_complex():
    assert basicMath.multiply((3 + 4j), (2 - 1j)) == (10 + 5j)

def test_multiply_when_boolean_true_false():
    assert basicMath.multiply(True, False) == 0
    
def test_multiply_when_boolean_true_true():
    assert basicMath.multiply(True, True) == 1
    
def test_multiply_when_boolean_false_false():
    assert basicMath.multiply(False, False) == 0

def test_multiply_when_lists_given():
    x = ["apple", "banana"]
    y = ["cherry"]
    with pytest.raises(Exception):
        basicMath.multiply(x, y)

def test_multiply_when_list_given_and_int():
    x = ["apple", "banana"]
    y = 1
    assert basicMath.multiply(x, y) == ["apple", "banana"]

def test_multiply_when_given_zeros():
    assert basicMath.multiply(0, 0) == 0

def test_multiply_when_first_number_is_zero():
    assert basicMath.multiply(0, 2) == 0

def test_multiply_when_second_numer_is_zero():
    assert basicMath.multiply(2, 0) == 0

# divide
def test_divide_when_positive_integer_given():
    assert basicMath.divide(3, 4) == 0.75

def test_divide_when_negative_integer_given():
    assert basicMath.divide(-3, -5) == 0.6
    
def test_divide_when_one_negative_integer():
    assert basicMath.divide(-3, 5) == -0.6

def test_divide_when_string_given():
    with pytest.raises(Exception):
        basicMath.divide("Hi ", "test")

def test_divide_when_one_string_given():
    with pytest.raises(Exception):
        basicMath.divide("Hi ", 1)

def test_divide_when_float_given():
    assert basicMath.divide(4.5, 1.5) == 3

def test_divide_when_one_float_given():
    assert basicMath.divide(3, 1.5) == 2

def test_divide_when_negative_float_given():
    assert basicMath.divide(2, -2.5) == -0.8

def test_divide_when_complex():
    assert basicMath.divide((3 + 4j), (2 - 1j)) == (0.4 + 2.2j)

def test_divide_when_boolean_true_false():
    with pytest.raises(Exception):
        basicMath.divide(True, False)
    
def test_divide_when_boolean_true_true():
    assert basicMath.divide(True, True) == 1
    
def test_divide_when_boolean_false_false():
    with pytest.raises(Exception):
        basicMath.divide(False, False)

def test_divide_when_lists_given():
    x = ["apple", "banana"]
    y = ["cherry"]
    with pytest.raises(Exception):
        basicMath.divide(x, y)

def test_divide_when_list_given_and_int():
    x = ["apple", "banana"]
    y = 1
    with pytest.raises(Exception):
        basicMath.divide(x, y)

def test_divide_when_given_zeros():
    with pytest.raises(Exception):
        basicMath.divide(0, 0)

def test_divide_when_first_number_is_zero():
    assert basicMath.divide(0, 2) == 0

def test_divide_when_second_numer_is_zero():
    with pytest.raises(Exception):
        basicMath.divide(2, 0)