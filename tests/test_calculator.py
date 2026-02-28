```python
# tests/test_calculator.py

import pytest
from app.calculator import calculate_discount

def test_calculate_discount_success():
    """Test calculate_discount function with a price above 100"""
    price = 150
    result = calculate_discount(price)
    assert result == price * 0.8

def test_calculate_discount_failure():
    """Test calculate_discount function with a price below 100"""
    price = 50
    result = calculate_discount(price)
    assert result == price * 0.9

def test_calculate_discount_edge_case():
    """Test calculate_discount function with a price exactly at 100"""
    price = 100
    result = calculate_discount(price)
    assert result == price * 0.9

def test_calculate_discount_invalid_input():
    """Test calculate_discount function with a non-numeric price"""
    price = 'abc'
    with pytest.raises(TypeError):
        calculate_discount(price)
```