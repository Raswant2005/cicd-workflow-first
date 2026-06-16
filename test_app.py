import pytest
from app import add, div , Company

def test_add():
    assert add(2, 3) == 5
    
    
def test_div():
    with pytest.raises((ValueError , ZeroDivisionError)):
        div(10, 0)
   
@pytest.mark.parametrize("x1,y1,expected", [
    (10, 2, 5),
    (15, 3, 5),
    (20, 4, 5)
])
def test_div_parametrized(x1, y1, expected):
    assert div(x1, y1) == expected
    
    
    
@pytest.fixture
def company():
    return Company()


@pytest.mark.parametrize("employee_id,name,expected", [
    (1, "John Doe", None),
    (1, "Jane Doe", ValueError("Employee with this ID already exists"))
])
def test_add_employee_parametrized(company, employee_id, name, expected):
    company.add_employee(employee_id, name)
    if expected is not None:
        with pytest.raises(ValueError, match=str(expected)):
            company.add_employee(employee_id, name)

def test_add_employee(company): 
    company.add_employee(1,"John Doe")
    with pytest.raises(ValueError, match="Employee with this ID already exists"):
        company.add_employee(1,"Jane Doe")
    
def get_employee_not_exists(company):
    with pytest.raises(ValueError, match="Employee with this ID does not exist"):
        company.get_employee(999) 
        
def test_delete_employee(company):
    company.add_employee(2,"Jane Doe")
    company.delete_employee(2)
    with pytest.raises(ValueError, match="Employee with this ID does not exist"):
        company.get_employee(2)