import pytest
from main import add
@pytest.mark.regression
def test_add_basic():
    assert add(1, 2) == 3

@pytest.mark.regression
def test_add_zero():
    assert add(0, 0) == 0

@pytest.mark.non_regression
def test_external_api():
    import requests
    response = requests.get("https://httpbin.org/get")
    assert response.status_code == 200
def test_add():
    assert add(2, 3) == 5
