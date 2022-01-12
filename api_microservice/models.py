# ######################################################################################################################
# ########################################                               ###############################################
# ########################################       SQLAlchemy Models       ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class Airplane(Base):
    __tablename__ = "airplane"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type_id = Column(Integer, ForeignKey("airplane_type.id"), nullable=False)


class AirplaneType(Base):
    __tablename__ = "airplane_type"
    id = Column(Integer, primary_key=True)
    max_capacity = Column(Integer, nullable=False)


class Airport(Base):
    __tablename__ = "airport"
    iata_id = Column(String, primary_key=True)
    city = Column(String)
    name = Column(String(255))
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    elevation = Column(Integer, nullable=False, default=1000)


class Flight(Base):
    __tablename__ = "flight"
    id = Column(Integer, primary_key=True, autoincrement=True)
    route_id = Column(Integer, ForeignKey("route.id"), nullable=False)
    airplane_id = Column(Integer, ForeignKey("airplane.id"), nullable=False)
    departure_time = Column(DateTime)
    reserved_seats = Column(Integer, nullable=False, default=0)
    seat_price = Column(Float, nullable=False, default=0.00)


class Route(Base):
    __tablename__ = "route"
    id = Column(Integer, primary_key=True, autoincrement=True)
    origin_id = Column(String, ForeignKey("airport.iata_id"), nullable=False)
    destination_id = Column(String, ForeignKey("airport.iata_id"), nullable=False)
    duration = Column(Integer, nullable=False)
