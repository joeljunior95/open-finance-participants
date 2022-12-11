from flask import current_app as app
from src.participant.participant_model import Participant
from src.participant.participant_model import ParticipantList

class ParticipantController:
    def __init__(self):
        pass

    def get_all(self):
        participantsList = ParticipantList()
        all_participants = participantsList.get_all()
        participants = [participant.serialize() for participant in all_participants]
        return participants

    def update_all(self, raw_data):
        participantsList = ParticipantList()
        participantsList.renew(raw_data)