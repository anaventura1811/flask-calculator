from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.calculators.interfaces.calculator_interface import CalculatorInterface


class Calculator4(CalculatorInterface):
    def calculate(self, request: FlaskRequest):  # type: ignore
        input_data = request.json
        numbers = self.__validate_body(input_data)
        average = self.__average(numbers)
        response = self.__format_response(average)
        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError('body mal formatado!')
        numbers = body["numbers"]
        if not isinstance(numbers, List) or (
              isinstance(numbers, List) and len(numbers) == 0):
            raise HttpUnprocessableEntityError('erro no formato do body!')
        return numbers

    def __average(self, numbers: List[float]) -> float:
        average_number = 0
        for num in numbers:
            average_number += num
        result = average_number / len(numbers)
        return result

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": average,
            }
        }
