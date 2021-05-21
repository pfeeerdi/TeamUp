from app import db
from sqlalchemy import desc, Index
from datetime import datetime

teamsurveys = db.Table(
    'teamsurveys',
    db.Column('survey_id', db.Integer, db.ForeignKey('surveys.survey_id')),
    db.Column('team_id', db.Integer, db.ForeignKey('teams.team_id'))
)# Survey-Team Mapping

class Survey(db.Model):
    __tablename__ = 'surveys'
    survey_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    question = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.today())
    team_id = db.relationship('Team', secondary=teamsurveys, back_populates="surveys")#backref=db.backref('surveys', lazy='dynamic'))


Index('survey_creator_date', Survey.creation_date.desc())

