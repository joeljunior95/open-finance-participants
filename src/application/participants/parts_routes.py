from flask import (
    render_template, request, redirect, Blueprint, Response,
    current_app as app, flash, url_for
)

parts_bp = Blueprint('parts_bp',__name__)

@parts_bp.route('/')
def index():
    return "JOIA"

@parts_bp.route('/oi')
def oi():
    return "HELLO"