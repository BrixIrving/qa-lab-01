import pytest
from src.division import dividir

def test_dividir():
    assert dividir(10, 2) == 5

def test_division_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)