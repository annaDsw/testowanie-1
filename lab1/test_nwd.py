import nwd
import pytest

# NWD iteration
def test_nwd_iteration_given_one():
    assert nwd.nwd_iteration(1, 1) == 1

def test_nwd_iteration_given_valid_numbers():
    assert nwd.nwd_iteration(120, 9) == 3

def test_nwd_iteration_given_zero():
    with pytest.raises(Exception):
        nwd.nwd_iteration(2, 0)

def test_nwd_iteration_given_string():
    with pytest.raises(Exception):
        nwd.nwd_iteration("0", "9")
        
def test_nwd_iteration_given_array():
    with pytest.raises(Exception):
        nwd.nwd_iteration([1, 3, 2], 2)

def test_nwd_iteration_given_negative_number():
    with pytest.raises(Exception):
        nwd.nwd_iteration(-2, 2)

def test_nwd_iteration_given_float():
    with pytest.raises(Exception):
        nwd.nwd_iteration(2, 2.4)

def test_nwd_iteration_given_complex():
    with pytest.raises(Exception):
        nwd.nwd_iteration(2, 1 + 1j)
    
def test_nwd_iteration_given_false():
    with pytest.raises(Exception):
        nwd.nwd_iteration(1, False)
        
def test_nwd_iteration_given_true():
    with pytest.raises(Exception):
        nwd.nwd_iteration(2, True)

# NWD recursive
def test_nwd_recursive_given_one():
    assert nwd.nwd_recursive(1, 1) == 1

def test_nwd_recursive_given_valid_numbers():
    assert nwd.nwd_recursive(120, 9) == 3

def test_nwd_recursive_given_zero():
    with pytest.raises(Exception):
        nwd.nwd_recursive(2, 0)

def test_nwd_recursive_given_string():
    with pytest.raises(Exception):
        nwd.nwd_recursive("0", "9")
        
def test_nwd_recursive_given_array():
    with pytest.raises(Exception):
        nwd.nwd_recursive([1, 3, 2], 2)

def test_nwd_recursive_given_negative_number():
    with pytest.raises(Exception):
        nwd.nwd_recursive(-2, 2)

def test_nwd_recursive_given_float():
    with pytest.raises(Exception):
        nwd.nwd_recursive(2, 2.4)

def test_nwd_recursive_given_complex():
    with pytest.raises(Exception):
        nwd.nwd_recursive(2, 1 + 1j)
    
def test_nwd_recursive_given_false():
    with pytest.raises(Exception):
        nwd.nwd_recursive(1, False)
        
def test_nwd_recursive_given_true():
    with pytest.raises(Exception):
        nwd.nwd_recursive(2, True)