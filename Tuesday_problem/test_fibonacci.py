import pytest
import Fibonacci

def test_Fibonacci_5():
    assert tuesday.Fibonacci(5) == 5

def test_Fibonacci_7():
    assert tuesday.Fibonacci(7) == 13

def test_Fibonacci_9():
    assert tuesday.Fibonacci(9) == 34

def test_Fibonacci_negative():
    assert tuesday.Fibonacci(-3) == 'please add a number greater than 0'

def test_Fibonacci_float():
    assert tuesday.Fibonacci(9.3) == 34