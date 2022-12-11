from flask import (
    render_template, request, redirect, Blueprint, Response,
    jsonify,
    current_app as app, flash, url_for
)
from flask_cors import cross_origin
import requests as re

from src.participant.participant_controller import ParticipantController

participant_bp = Blueprint(
    'participant_bp',
    __name__,
     url_prefix='/participants')

controller = ParticipantController()

@participant_bp.route('/')
@participant_bp.route('/list')
@cross_origin()
def list():
    data = controller.get_all()
    return jsonify(data)

@participant_bp.route('/update/all',methods=['PUT'])
def update_all():
    print('Updating all')
    r = re.get(app.config['API_OPENBANKING'])
    if r.status_code != 200:
        return jsonify(r.status_code,r.reason)
    controller.update_all(r.json())
    return jsonify(controller.get_all())