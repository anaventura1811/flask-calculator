from typing import Dict
from .calculator_1 import Calculator1


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator1 = Calculator1()
    response = calculator1.calculate(mock_request)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]
    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1


def test_calculate_with_body_error():
    print('\nEstou aqui no teste 2')
    pass
