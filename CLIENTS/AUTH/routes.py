from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, current_app, json, session
from CLIENTS.settings import *
# from CLIENTS import login_manager
import requests

auth_bp = Blueprint("auth_bp", __name__, template_folder='templates', static_folder='static')

@auth_bp.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = request.form
        respi = requests.post(f"{SERVER_URL}/auth/register", data=data)
        resp = respi.json()
        print(resp)
        if respi.status_code == 409:
            return f"{resp['error']}"
        return render_template("auth/email_confirmation.html", title=APP_NAME, email=EMAIL, phone=PHONE, user_email=data['email'])
    return render_template("auth/register.html", title=APP_NAME, email=EMAIL, phone=PHONE)


@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.form
        return f"{data}"
    return render_template("auth/login.html", title=APP_NAME, email=EMAIL, phone=PHONE)

@auth_bp.route("/email_confirmation", methods=["POST", "GET"])
def email_confirmation():
    if request.method == "POST":
        data = request.form
        resp = requests.post(f"{SERVER_URL}/auth/verify_email", data=data)
        return resp.json()
    return render_template("auth/email_confirmation.html", title=APP_NAME, email=EMAIL, phone=PHONE)






# Flask-Login user loader callback
# @login_manager.user_loader
# def load_user(user_id):
#     return AdminUser(user_id)