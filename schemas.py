# ######################################################################################################################
# ########################################                               ###############################################
# ########################################      Marshmallow Schemas      ###############################################
# ########################################                               ###############################################
# ######################################################################################################################
from flask_marshmallow import Marshmallow
from models import *

# Initializing Marshmallow Serialization Handler
ma = Marshmallow()


class AirplaneSchema(ma.Schema):
    class Meta:
        fields = ("id", "type_id")
        model = Airplane


airplane_schema = AirplaneSchema()
airplanes_schema = AirplaneSchema(many=True)


class AirplaneTypeSchema(ma.Schema):
    class Meta:
        fields = ("id", "max_capacity")
        model = AirplaneType


airplane_type_schema = AirplaneTypeSchema()
airplane_types_schema = AirplaneTypeSchema(many=True)


class AirportSchema(ma.Schema):
    class Meta:
        fields = ("iata_id", "city", "name", "longitude", "latitude", "elevation")
        model = Airport


airport_schema = AirportSchema()
airports_schema = AirportSchema(many=True)


class FlightSchema(ma.Schema):
    class Meta:
        fields = ("id", "route_id", "airplane_id", "departure_time", "reserved_seats", "seat_price")
        model = Flight


flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)


class RouteSchema(ma.Schema):
    class Meta:
        fields = ("id", "origin_id", "destination_id", "duration")
        model = Route


route_schema = RouteSchema()
routes_schema = RouteSchema(many=True)