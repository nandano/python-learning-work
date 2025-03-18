import pytest
from employee_class import Employee

@pytest.fixture
def employee():
    employee = Employee('bodhi', 'sattva', 100000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 105000

def test_give_custom_raise(employee):
    employee.give_raise(20000)
    assert employee.salary == 120000
