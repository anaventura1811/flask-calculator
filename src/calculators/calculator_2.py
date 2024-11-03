from typing import List, Dict
from flask import request as FlaskRequest
from src.drivers.numpy_handler import NumpyHandler


class Calculator2:
    '''
        N numeros são enviados (lista de numeros)
        Todos os numeros sao multiplicados por 11 e elevados a potencia de 0.95
        Por fim, é retirado o desvio padrão desses resultados e
        retornado o inverso desse valor (1/result)
    '''
    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body=body)
        # print(f"\n{input_data}")
        calc_number = self.__process_data(numbers=input_data)
        # print(calc_number)
        result = self.__format_response(calc_number)
        # print(result)
        return result

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception('body mal formatado!')
        numbers = body["numbers"]
        return numbers

    def __process_data(self, numbers: List[float]) -> float:
        numpy_handler = NumpyHandler()
        list_numbers = [(number * 11) ** 0.95 for number in numbers]
        result = numpy_handler.standard_derivation(list_numbers)
        return 1/result

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calc_result, 2)
            }
        }
