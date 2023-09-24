import fibonacci
import pytest

# Fibonacci iteration
def test_fibonacci_iteration_find_first():
    assert fibonacci.fibonacci_iteration(1) == 1

def test_fibonacci_iteration_find_second():
    assert fibonacci.fibonacci_iteration(2) == 1

def test_fibonacci_iteration_find_fourth():
    assert fibonacci.fibonacci_iteration(4) == 3

def test_fibonacci_iteration_find_eight():
    assert fibonacci.fibonacci_iteration(8) == 21

def test_fibonacci_iteration_given_zero():
    with pytest.raises(Exception):
        fibonacci.fibonacci_iteration(0)

def test_fibonacci_iteration_given_string():
    with pytest.raises(Exception):
        fibonacci.fibonacci_iteration("0")
        
def test_fibonacci_iteration_given_array():
    with pytest.raises(Exception):
        fibonacci.fibonacci_iteration([1, 3, 2])

def test_fibonacci_iteration_given_negative_number():
    with pytest.raises(Exception):
        fibonacci.fibonacci_iteration(-2)

def test_fibonacci_iteration_given_float():
    with pytest.raises(Exception):
        fibonacci.fibonacci_iteration(2.4)

def test_fibonacci_iteration_given_complex():
    with pytest.raises(Exception):
        fibonacci.fibonacci_iteration(1 + 1j)
    
def test_fibonacci_iteration_given_false():
    with pytest.raises(Exception):
        fibonacci.fibonacci_iteration(False)
        
def test_fibonacci_iteration_given_true():
    with pytest.raises(Exception):
        fibonacci.fibonacci_iteration(True)

# Fibonacci recursion
def test_fibonacci_find_first():
    assert fibonacci.fibonacci_recursion(1) == 1

def test_fibonacci_find_second():
    assert fibonacci.fibonacci_recursion(2) == 1

def test_fibonacci_find_fourth():
    assert fibonacci.fibonacci_recursion(4) == 3

def test_fibonacci_find_eight():
    assert fibonacci.fibonacci_recursion(8) == 21

def test_fibonacci_given_zero():
    with pytest.raises(Exception):
        fibonacci.fibonacci_recursion(0)

def test_fibonacci_given_string():
    with pytest.raises(Exception):
        fibonacci.fibonacci_recursion("0")
        
def test_fibonacci_given_array():
    with pytest.raises(Exception):
        fibonacci.fibonacci_recursion([1, 3, 2])

def test_fibonacci_given_negative_number():
    with pytest.raises(Exception):
        fibonacci.fibonacci_recursion(-2)

def test_fibonacci_given_float():
    with pytest.raises(Exception):
        fibonacci.fibonacci_recursion(2.4)

def test_fibonacci_given_complex():
    with pytest.raises(Exception):
        fibonacci.fibonacci_recursion(1 + 1j)
    
def test_fibonacci_given_false():
    with pytest.raises(Exception):
        fibonacci.fibonacci_recursion(False)
        
def test_fibonacci_given_true():
    with pytest.raises(Exception):
        fibonacci.fibonacci_recursion(True)