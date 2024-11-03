from typing import List, Dict
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_hdr_interface import DriverHandlerInterface
from src.calculators.interfaces.calculator_interface import CalculatorInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError


class Calculator3(CalculatorInterface):
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest):  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance=variance, multiplication=multiplication)

        response = self.__format_response(variance=variance)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
        numbers = body["numbers"]
        return numbers

    def __calculate_variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication

    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError(
                'Falha no processo: Variância menor que multiplicação')

    def __format_response(self, variance: float) -> Dict:
        return {
          "data": {
              "Calculator": 3,
              "value": variance,
              "success": True,
          }
        }
