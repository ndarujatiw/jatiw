#employee.py
class Employee:
    """A class representing an employee profile and salary."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add a specified amount to the annual salary (default is $5,000)."""
        self.annual_salary += amount
        
    #test_employee.py
    
    #without fixture
    from employee import Employee


def test_give_default_raise():
    """Test that a default raise of $5,000 works correctly."""
    emp = Employee("Ada", "Lovelace", 75000)
    emp.give_raise()
    assert emp.annual_salary == 80000


def test_give_custom_raise():
    """Test that a custom raise amount works correctly."""
    emp = Employee("Ada", "Lovelace", 75000)
    emp.give_raise(10000)
    assert emp.annual_salary == 85000
    
#with fixture
import pytest
from employee import Employee


@pytest.fixture
def employee():
    """A shared Employee instance available for test functions."""
    return Employee("Ada", "Lovelace", 75000)


def test_give_default_raise(employee):
    """Test that a default raise of $5,000 works correctly."""
    employee.give_raise()
    assert employee.annual_salary == 80000


def test_give_custom_raise(employee):
    """Test that a custom raise amount works correctly."""
    employee.give_raise(10000)
    assert employee.annual_salary == 85000
    
#run pytest