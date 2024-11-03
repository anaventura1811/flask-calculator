from src.calculators.calculator_4 import Calculator4
from typing import Dict
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4]})
    calc = Calculator4()
    response = calc.calculate(mock_request)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "value" in response["data"]
    assert response == {'data': {'Calculator': 4, 'value': 2.5}}


def test_calculator_error():
    mock_request = MockRequest(body={"teste": 1})
    calc = Calculator4()
    with raises(Exception) as infoexcept:
        calc.calculate(mock_request)
    assert str(infoexcept.value) == 'body mal formatado!'


def test_calculate_error_2():
    mock_request = MockRequest(body={"numbers": 1})
    calc = Calculator4()
    with raises(Exception) as infoexcept:
        calc.calculate(mock_request)
    assert str(infoexcept.value) == 'erro no formato do body!'


def test_calculate_error_3():
    mock_request = MockRequest(body={"numbers": []})
    calc = Calculator4()
    with raises(Exception) as infoexcept:
        calc.calculate(mock_request)
    assert str(infoexcept.value) == 'erro no formato do body!'
