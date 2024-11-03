from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler


def calculator3_factory():
    driver = NumpyHandler()
    calc = Calculator3(driver_handler=driver)
    return calc
