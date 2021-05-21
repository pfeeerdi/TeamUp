from app import db
from sqlalchemy import desc, Index
from datetime import datetime
from .team import teammembers
from .survey_options import survey_votes


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    lastName = db.Column(db.String, nullable=False)
    firstName = db.Column(db.String, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    join_date = db.Column(db.DateTime, nullable=False, default=datetime.today())
    teams = db.relationship('Team', secondary=teammembers, back_populates="members")
    survey_votes = db.relationship('Survey_Options', secondary=survey_votes, back_populates="votes")


Index('user_lastname_idx', User.lastName.desc())
