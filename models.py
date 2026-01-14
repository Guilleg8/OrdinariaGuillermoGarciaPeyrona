from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


# tabla de usuarios (residentes)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)  # En producción usar hash


# tabla de servicios (gimnasio, piscina, etc.)
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    max_capacity = db.Column(db.Integer, nullable=False)


# tabla de reservas
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date = db.Column(db.String(20), nullable=False)  # Formato YYYY-MM-DD
    time_slot = db.Column(db.String(10), nullable=False)  # Ej: "10:00"

    # relaciones para acceder a los datos fácilmente
    user = db.relationship('User', backref='reservations')
    service = db.relationship('Service')