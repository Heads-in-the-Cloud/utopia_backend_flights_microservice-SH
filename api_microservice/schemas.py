# ######################################################################################################################
# ########################################                               ###############################################
# ########################################        Pydantic Schemas       ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
import datetime
from typing import List, Optional

from pydantic import BaseModel


# ------------------------------------------------
#                   Airplane
# ------------------------------------------------


class Airplane(BaseModel):
    type_id: int


class AirplaneUpdate(BaseModel):
    type_id: Optional[int] = None


class AirplaneFull(Airplane):
    id: int

    class Config:
        orm_mode = True


# ------------------------------------------------
#                 Airplane Type
# ------------------------------------------------


class AirplaneType(BaseModel):
    max_capacity: int


class AirplaneTypeUpdate(BaseModel):
    max_capacity: Optional[int] = None


class AirplaneTypeFull(AirplaneType):
    id: int

    class Config:
        orm_mode = True


# ------------------------------------------------
#                   Airports
# ------------------------------------------------


class Airport(BaseModel):
    iata_id: str
    city: str
    name: str = ""
    longitude: float
    latitude: float
    elevation: int = 0

    class Config:
        orm_mode = True


class AirportUpdate(BaseModel):
    iata_id: Optional[str] = None
    city: Optional[str] = None
    name: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    elevation: Optional[int] = None


# ------------------------------------------------
#                      Flight
# ------------------------------------------------


class Flight(BaseModel):
    route_id: int
    airplane_id: int
    departure_time: datetime.datetime
    reserved_seats: int
    seat_price: float


class FlightUpdate(BaseModel):
    route_id: Optional[int] = None
    airplane_id: Optional[int] = None
    departure_time: Optional[datetime.datetime] = None
    reserved_seats: Optional[int] = None
    seat_price: Optional[float] = None


class FlightFull(Flight):
    id: int

    class Config:
        orm_mode = True


# ------------------------------------------------
#                      Route
# ------------------------------------------------


class Route(BaseModel):
    origin_id: str
    destination_id: str
    duration: int


class RouteUpdate(BaseModel):
    origin_id: Optional[str] = None
    destination_id: Optional[str] = None
    duration: Optional[int] = None

class RouteFull(Route):
    id: int

    class Config:
        orm_mode = True
