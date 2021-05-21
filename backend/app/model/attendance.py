from app import db
from sqlalchemy import Index, true, false


class Attendance(db.Model):
    __tablename__ = 'attendance'
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.appointment_id'), primary_key=True)
    attendee_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    status = db.Column(db.Boolean, nullable=False)

Index('attendance_true',
      Attendance.status,
      postgresql_where=(Attendance.status == true())
      )
Index('attendance_false',
      Attendance.status,
      postgresql_where=(Attendance.status == false())
      )
