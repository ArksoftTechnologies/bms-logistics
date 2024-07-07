from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, current_app, json, session
from CLIENTS.settings import *
import requests

home_bp = Blueprint("home_bp", __name__, template_folder='templates', static_folder='static')

@home_bp.route("/", methods=["POST", "GET"])
def index():
    return render_template('home/index.html', title=APP_NAME, email=EMAIL, phone=PHONE)

@home_bp.route("/place_order", methods=["POST"])
def place_order():
    data = request.form
    print(data)
    # resp = requests.post(SERVER_URL, data=data)
    # resp = resp.json()
    return "Successful"

