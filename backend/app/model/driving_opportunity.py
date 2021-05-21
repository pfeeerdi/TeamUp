from app import db

passengers = db.Table(
    'passengers',
    db.Column('appointment_id', db.Integer),
    db.Column('driver_id', db.Integer),
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id')),
    db.ForeignKeyConstraint(['appointment_id', 'driver_id'], ['driving_opportunity.appointment_id', 'driving_opportunity.driver_id'])
)  # Driving Opportunity - Users Mapping


class Driving_Opportunity(db.Model):
    __tablename__ = 'driving_opportunity'
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.appointment_id'), primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    max_passengers = db.Column(db.Integer, nullable=False) #excluding the driver
    passengers = db.relationship('User', secondary=passengers, backref=db.backref('driving_opportunities', lazy='dynamic'))


