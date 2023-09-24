import silnia
import pytest

# Silnia iteration
def test_fibonacci_iteration_given_one():
    assert silnia.silnia_iteration(1) == 1

def test_fibonacci_iteration_given_two():
    assert silnia.silnia_iteration(2) == 2

def test_fibonacci_iteration_given_four():
    assert silnia.silnia_iteration(4) == 24

def test_silnia_iteration_given_five():
    assert silnia.silnia_iteration(5) == 120

def test_silnia_iteration_given_zero():
    assert silnia.silnia_iteration(0) == 1

def test_silnia_iteration_given_string():
    with pytest.raises(Exception):
        silnia.silnia_iteration("0")
        
def test_silnia_iteration_given_array():
    with pytest.raises(Exception):
        silnia.silnia_iteration([1, 3, 2])

def test_silnia_iteration_given_negative_number():
    with pytest.raises(Exception):
        silnia.silnia_iteration(-2)

def test_silnia_iteration_given_float():
    with pytest.raises(Exception):
        silnia.silnia_iteration(2.4)

def test_silnia_iteration_given_complex():
    with pytest.raises(Exception):
        silnia.silnia_iteration(1 + 1j)
    
def test_silnia_iteration_given_false():
    with pytest.raises(Exception):
        silnia.silnia_iteration(False)
        
def test_silnia_iteration_given_true():
    with pytest.raises(Exception):
        silnia.silnia_iteration(True)


# Silnia recursion
def test_silnia_recursive_given_one():
    assert silnia.silnia_recursive(1) == 1

def test_silnia_recursive_given_two():
    assert silnia.silnia_recursive(2) == 2

def test_silnia_recursive_given_four():
    assert silnia.silnia_recursive(4) == 24

def test_silnia_recursive_given_five():
    assert silnia.silnia_recursive(5) == 120

def test_silnia_recursive_given_zero():
    assert silnia.silnia_recursive(0) == 1

def test_silnia_recursive_given_string():
    with pytest.raises(Exception):
        silnia.silnia_recursive("0")
        
def test_silnia_recursive_given_array():
    with pytest.raises(Exception):
        silnia.silnia_recursive([1, 3, 2])

def test_silnia_recursive_given_negative_number():
    with pytest.raises(Exception):
        silnia.silnia_recursive(-2)

def test_silnia_recursive_given_float():
    with pytest.raises(Exception):
        silnia.silnia_recursive(2.4)

def test_silnia_recursive_given_complex():
    with pytest.raises(Exception):
        silnia.silnia_recursive(1 + 1j)
    
def test_silnia_recursive_given_false():
    with pytest.raises(Exception):
        silnia.silnia_recursive(False)
        
def test_silnia_recursive_given_true():
    with pytest.raises(Exception):
        silnia.silnia_recursive(True)
