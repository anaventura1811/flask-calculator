from flask import Blueprint, jsonify, request
from src.main.factories.calculator_2_factory import calculator2_factory
from src.main.factories.calculator_1_factory import calculator1_factory

calc_route_bp = Blueprint("calc_routes", __name__)


@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = calculator1_factory()
    response = calc.calculate(request)
    return jsonify(response)


@calc_route_bp.route('/calculator/2', methods=['POST'])
def calculator_2():
    calc = calculator2_factory()
    response = calc.calculate(request)
    return jsonify(response)
