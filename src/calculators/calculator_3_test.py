from typing import Dict, List
from pytest import raises
from src.calculators.calculator_3 import Calculator3
from src.drivers.interfaces.driver_hdr_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return super().standard_derivation(numbers)

    def variance(self, numbers: List[float]) -> float:
        return 1568.16


class MockDriverHandlerError(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        return super().standard_derivation(numbers)

    def variance(self, numbers: List[float]) -> float:
        return 3


# Teste de integração entre numpy handler e calculator3
def test_calculate_with_variance_error():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver = MockDriverHandlerError()
    calculator_3 = Calculator3(driver_handler=driver)
    with raises(Exception) as infoexecpt:
        calculator_3.calculate(mock_request)
    error_msg = 'Falha no processo: Variância menor que multiplicação'
    assert str(infoexecpt.value) == error_msg


# Teste de integração entre numpy handler e calculator3
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    driver = MockDriverHandler()
    calculator_3 = Calculator3(driver_handler=driver)
    response = calculator_3.calculate(mock_request)
    assert response == {'data':
                        {'Calculator': 3, 'value': 1568.16, 'success': True}}


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    driver = MockDriverHandler()
    calculator_3 = Calculator3(driver_handler=driver)
    response = calculator_3.calculate(mock_request)
    assert response == {'data':
                        {'Calculator': 3, 'value': 1568.16, 'success': True}}
