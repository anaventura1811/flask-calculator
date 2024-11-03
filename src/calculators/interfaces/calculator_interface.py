from abc import ABC, abstractmethod
from flask import request as FlaskRequest


class CalculatorInterface(ABC):

    @abstractmethod
    def calculate(self, request: FlaskRequest):  # type: ignore
        pass
