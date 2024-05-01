from employee import Employee

def test_give_default_raise():
    """Test that a default raise is given"""
    eleo = Employee("Eleonora", "Cordova", 1000)
    assert eleo.give_raise() == 6000 

def test_custom_raise():
    """Test that a custom raise is given"""
    eleo = Employee("Eleonora", "Cordova", 1000)
    assert eleo.give_raise(1000) == 2000