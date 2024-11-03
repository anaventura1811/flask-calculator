from src.calculators.calculator_2 import Calculator2
from typing import Dict


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate_2():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    calculator_2 = Calculator2()
    response = calculator_2.calculate(mock_request)
    assert isinstance(response, dict)
    assert response == {'data': {'Calculator': 2, 'result': 0.08}}
