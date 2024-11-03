from src.calculators.calculator_2 import Calculator2
from typing import Dict
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


# Teste de integração entre numpy handler e calculator2
def test_calculate_integration():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver_handler=driver)
    response = calculator_2.calculate(mock_request)
    assert isinstance(response, dict)
    assert response == {'data': {'Calculator': 2, 'result': 0.08}}
