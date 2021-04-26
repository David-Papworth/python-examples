import pytest
import even_between

def test_count_short():
    assert even_between(10, 30) = 20, 22, 24, 26, 28

def test_count_long():
    assert even_between(2, 50) = 2, 4, 6, 8, 20, 22, 24, 26, 28, 42, 44, 46, 48