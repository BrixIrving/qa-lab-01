from src.temperatura import convertir_celsius_a_fahrenheit

def test_conversion_1():
    assert convertir_celsius_a_fahrenheit(0) == 32

def test_conversion_2():
    assert convertir_celsius_a_fahrenheit(100) == 212