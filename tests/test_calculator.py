import pytest
from app.calculator import calculate_discount

def test_calculate_discount_success():
    price = 150
    result = calculate_discount(price)
    assert result == price * 0.8

def test_calculate_discount_failure():
    price = 50
    result = calculate_discount(price)
    assert result == price * 0.9

def test_calculate_discount_edge_case():
    price = 100
    result = calculate_discount(price)
    assert result == price * 0.9

def test_calculate_discount_invalid_input():
    with pytest.raises(TypeError):
        calculate_discount("invalid_price")

def test_calculate_discount_zero_price():
    price = 0
    result = calculate_discount(price)
    assert result == price * 0.9