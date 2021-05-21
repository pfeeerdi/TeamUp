from app import db
from sqlalchemy import desc, Index
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime

teammembers = db.Table(
    'teammembers',
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.Column('team_id', db.Integer, db.ForeignKey('teams.team_id'))
) # User-Team Mapping

class Team(db.Model):
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, primary_key=True)
    admin_email = db.Column(db.String, nullable=False, unique=True)
    team_name = db.Column(db.String, nullable=False)
    share_code = db.Column(db.String, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.today())
    # trades = association_proxy('trades', ['debit_currency', 'credit_currency'])
    # portfolio = db.relationship('Portfolio', uselist=False, foreign_keys='Portfolio.user_id', cascade='all, delete-orphan', backref=db.backref('users', lazy=True), lazy=True)
    # posts = db.relationship('Post', backref='user', lazy='dynamic')
    #accounts = db.relationship("SocialMediaAccount", back_populates="user")

    members = db.relationship(
        'User', secondary=teammembers,
        back_populates="teams")

Index('team_teamname_idx', Team.team_name.desc())
