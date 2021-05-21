from app import db
from sqlalchemy import desc, Index
from sqlalchemy.ext.associationproxy import association_proxy
from datetime import datetime
from .team import teammembers


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    lastName = db.Column(db.String, nullable=False)
    firstName = db.Column(db.String, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    join_date = db.Column(db.DateTime, nullable=False, default=datetime.today())
    # trades = association_proxy('trades', ['debit_currency', 'credit_currency'])
    # portfolio = db.relationship('Portfolio', uselist=False, foreign_keys='Portfolio.user_id', cascade='all, delete-orphan', backref=db.backref('users', lazy=True), lazy=True)
    # posts = db.relationship('Post', backref='user', lazy='dynamic')
    # accounts = db.relationship("SocialMediaAccount", back_populates="user")

    teams = db.relationship(
        'Team', secondary=teammembers,
        back_populates="members")


Index('user_lastname_idx', User.lastName.desc())
