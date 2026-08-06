from project_quant.tenor import Tenor
import pytest

def test_years():
    assert Tenor("3M").years() == pytest.approx(0.25)
def test_string():
    assert str(Tenor("3M")) == "3M"
def test_invalid_unit():
    with pytest.raises(ValueError):
        Tenor("3X")
def test_negative_length():
    with pytest.raises(ValueError):
        Tenor("-3M")
def test_empty_tenor():
    with pytest.raises(ValueError):
        Tenor("")