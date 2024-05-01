import pytest
from employee import Employee

@pytest.fixture
def eleo_raise():
    eleo_raise = Employee("Eleonora", "Cordova", 1000)
    return eleo_raise

def test_default_raise(eleo_raise):
    """Test that a default raise is given"""
    assert eleo_raise.give_raise() == 6000

def test_custom_raise(eleo_raise):
    """Test that a custom raise is given"""
    assert eleo_raise.give_raise(1000) == 2000