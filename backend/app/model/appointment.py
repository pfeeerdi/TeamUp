from app import db
from sqlalchemy import desc, Index
from datetime import datetime

# teamsurveys = db.Table(
#     'teamsurveys',
#     db.Column('survey_id', db.Integer, db.ForeignKey('surveys.survey_id')),
#     db.Column('team_id', db.Integer, db.ForeignKey('teams.team_id'))
# )# Survey-Team Mapping

class Appointment(db.Model):
    __tablename__ = 'appointments'
    appointment_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'))
    title = db.Column(db.String, nullable=False)
    beginning_datetime = db.Column(db.DateTime, nullable=False, default=datetime.today())
    ending_datetime = db.Column(db.DateTime, nullable=False, default=datetime.today())
    location = db.Column(db.String, nullable=False)

Index('appointments_by_date', Appointment.beginning_datetime.desc())


