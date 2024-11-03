from typing import List, Dict
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_hdr_interface import DriverHandlerInterface
from src.calculators.interfaces.calculator_interface import CalculatorInterface


class Calculator2(CalculatorInterface):

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body=body)
        calc_number = self.__process_data(numbers=input_data)
        result = self.__format_response(calc_number)
        return result

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception('body mal formatado!')
        numbers = body["numbers"]
        return numbers

    def __process_data(self, numbers: List[float]) -> float:
        list_numbers = [(number * 11) ** 0.95 for number in numbers]
        result = self.__driver_handler.standard_derivation(list_numbers)
        return 1/result

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calc_result, 2)
            }
        }
