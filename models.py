# ######################################################################################################################
# ########################################                               ###############################################
# ########################################       SQLAlchemy Models       ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from flask_sqlalchemy import SQLAlchemy

# Initializing the SQLAlchemy Database ORM
db = SQLAlchemy()

# ------------------------------------------------
#                   Models Tables
# ------------------------------------------------


class Airplane(db.Model):
    __tablename__ = "airplane"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_id = db.Column(db.Integer, db.ForeignKey("airplane_type.id"), nullable=False)


class AirplaneType(db.Model):
    __tablename__ = "airplane_type"
    id = db.Column(db.Integer, primary_key=True)
    max_capacity = db.Column(db.Integer, nullable=False)


class Airport(db.Model):
    __tablename__ = "airport"
    iata_id = db.Column(db.String, primary_key=True)
    city = db.Column(db.String)
    name = db.Column(db.String(255))
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    elevation = db.Column(db.Integer, nullable=False, default=1000)


class Flight(db.Model):
    __tablename__ = "flight"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    route_id = db.Column(db.Integer, db.ForeignKey("route.id"), nullable=False)
    airplane_id = db.Column(db.Integer, db.ForeignKey("airplane.id"), nullable=False)
    departure_time = db.Column(db.DateTime)
    reserved_seats = db.Column(db.Integer, nullable=False, default=0)
    seat_price = db.Column(db.Float, nullable=False, default=0.00)


class Route(db.Model):
    __tablename__ = "route"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    origin_id = db.Column(db.String, db.ForeignKey("airport.iata_id"), nullable=False)
    destination_id = db.Column(db.String, db.ForeignKey("airport.iata_id"), nullable=False)
    duration = db.Column(db.Integer, nullable=False)


# ------------------------------------------------
#                   Association Tables
# ------------------------------------------------


booking_agent = db.Table(
    "booking_agent",
    db.metadata,
    db.Column("booking_id", db.Integer, db.ForeignKey("booking.id"), primary_key=True),
    db.Column("agent_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)


booking_user = db.Table(
    "booking_user",
    db.metadata,
    db.Column("booking_id", db.Integer, db.ForeignKey("booking.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True)
)


flight_booking = db.Table(
    "flight_booking",
    db.metadata,
    db.Column("flight_id", db.Integer, db.ForeignKey("flight.id"), primary_key=True),
    db.Column("booking_id", db.Integer, db.ForeignKey("booking.id"), primary_key=True)
)
