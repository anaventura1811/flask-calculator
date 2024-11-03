from flask import Flask
from src.main.routes.calculators import calc_route_bp
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(calc_route_bp)
