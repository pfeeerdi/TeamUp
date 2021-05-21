from app import db
from datetime import datetime

survey_votes = db.Table(
    'survey_votes',
    db.Column('survey_id', db.Integer),
    db.Column('some_option', db.String),
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.ForeignKeyConstraint(['survey_id', 'some_option'], ['survey_options.survey_id', 'survey_options.some_option'])
)  # Survey_Options-User Mapping


class Survey_Options(db.Model):
    __tablename__ = 'survey_options'
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.survey_id'), primary_key=True)
    some_option = db.Column(db.String, nullable=False, primary_key=True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.today())
    votes = db.relationship('User', secondary=survey_votes, back_populates="survey_votes")