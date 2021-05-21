from app import db
from sqlalchemy import desc, Index
from datetime import datetime
from .survey import teamsurveys

teammembers = db.Table(
    'teammembers',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.Column('team_id', db.Integer, db.ForeignKey('teams.team_id'))
) # User-Team Mapping

class Team(db.Model):
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    team_name = db.Column(db.String, nullable=False)
    share_code = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.today())
    members = db.relationship('User', secondary=teammembers, back_populates="teams")#backref=db.backref('teams', lazy='dynamic'))
    surveys = db.relationship('Survey', secondary=teamsurveys, back_populates="team_id")


Index('team_teamname_idx', Team.team_name.desc())

