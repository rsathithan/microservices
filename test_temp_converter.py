"""
test cases for pytest
"""

import math

#pytest test cases for temp converter

from temp_converter_rich import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)

def is_close(a, b, rel_tol=1e-9):
    return math.isclose(a, b, rel_tol=rel_tol)

def test_celsius_to_fahrenheit():
    assert is_close(celsius_to_fahrenheit(0), 32)
    assert is_close(celsius_to_fahrenheit(100), 212)
    assert is_close(celsius_to_fahrenheit(-40), -40)

def test_fahrenheit_to_celsius():
    assert is_close(fahrenheit_to_celsius(32), 0)
    assert is_close(fahrenheit_to_celsius(212), 100)
    assert is_close(fahrenheit_to_celsius(-40), -40)

def test_celsius_to_kelvin():
    assert is_close(celsius_to_kelvin(0), 273.15)
    assert is_close(celsius_to_kelvin(-273.15), 0)

def test_kelvin_to_celsius():
    assert is_close(kelvin_to_celsius(273.15), 0)
    assert is_close(kelvin_to_celsius(0), -273.15)
