# ######################################################################################################################
# ########################################                               ###############################################
# ########################################        Restful Resources      ###############################################
# ########################################                               ###############################################
# ######################################################################################################################

from flask import request
from flask_restful import Resource, Api

from schemas import *


# ------------------------------------------------
#                   Airport
# ------------------------------------------------


class AirportResource(Resource):
    def get(self, iata_id):
        airport = Airport.query.get_or_404(iata_id)
        return airport_schema.dump(airport)


class AirportListResource(Resource):
    def get(self):
        airports = Airport.query.all()
        return airports_schema.dump(airports)


class AirportCreationResource(Resource):
    def post(self):
        new_airport = Airport(
            iata_id=request.json['iata_id'],
            city=request.json['city'],
            name=request.json['name'],
            longitude=request.json['longitude'],
            latitude=request.json['latitude'],
            elevation=request.json['elevation']
        )
        db.session.add(new_airport)
        db.session.commit()
        return airplane_schema.dump(new_airport)


class AirportPatchResource(Resource):
    def post(self, iata_id):
        airport = Airport.query.get_or_404(iata_id)

        if 'iata_id' in request.json:
            airport.iata_id = request.json['iata_id']
        if 'city' in request.json:
            airport.city = request.json['city']
        if 'name' in request.json:
            airport.name = request.json['name']
        if 'longitude' in request.json:
            airport.longitude = request.json['longitude']
        if 'latitude' in request.json:
            airport.latitude = request.json['latitude']
        if 'elevation' in request.json:
            airport.elevation = request.json['elevation']

        db.session.commit()
        return airport_schema.dump(airport)


class AirportDeleteResource(Resource):
    def post(self, iata_id):
        airport = Airport.query.get_or_404(iata_id)

        db.session.delete(airport)
        db.session.commit()
        return '', 204


# ------------------------------------------------
#                   Airplane
# ------------------------------------------------

class AirplaneResource(Resource):
    def get(self, airplane_id):
        airplane = Airplane.query.get_or_404(airplane_id)
        return airplane_schema.dump(airplane)


class AirplaneListResource(Resource):
    def get(self):
        airplanes = Airplane.query.all()
        return airplanes_schema.dump(airplanes)


class AirplaneCreationResource(Resource):
    def post(self):
        new_airplane = Airplane(
            type_id=request.json['type_id']
        )
        db.session.add(new_airplane)
        db.session.commit()
        return airplane_schema.dump(new_airplane)


class AirplanePatchResource(Resource):
    def post(self, airplane_id):
        airplane = Airplane.query.get_or_404(airplane_id)

        if 'airplane_id' in request.json:
            airplane.id = request.json['airplane_id']
        if 'city' in request.json:
            airplane.type_id = request.json['type_id']

        db.session.commit()
        return airplane_schema.dump(airplane)


class AirplaneDeleteResource(Resource):
    def post(self, airplane_id):
        airplane = Airplane.query.get_or_404(airplane_id)

        db.session.delete(airplane)
        db.session.commit()
        return '', 204


# ------------------------------------------------
#                 Airplane Type
# ------------------------------------------------

class AirplaneTypeResource(Resource):
    def get(self, airplane_type_id):
        airplane_type = AirplaneType.query.get_or_404(airplane_type_id)
        return airplane_type_schema.dump(airplane_type)


class AirplaneTypeListResource(Resource):
    def get(self):
        airplane_types = AirplaneType.query.all()
        return airplane_types_schema.dump(airplane_types)


class AirplaneTypeCreationResource(Resource):
    def post(self):
        new_airplane_type = AirplaneType(
            id=request.json['type_id'],
            max_capacity=request.json['max_capacity']
        )
        db.session.add(new_airplane_type)
        db.session.commit()
        return airplane_type_schema.dump(new_airplane_type)


class AirplaneTypePatchResource(Resource):
    def post(self, airplane_type_id):
        airplane_type = AirplaneType.query.get_or_404(airplane_type_id)

        if 'type_id' in request.json:
            airplane_type.id = request.json['type_id']
        if 'city' in request.json:
            airplane_type.max_capacity = request.json['max_capacity']

        db.session.commit()
        return airplane_type_schema.dump(airplane_type)


class AirplaneTypeDeleteResource(Resource):
    def post(self, airplane_type_id):
        airplane_type = Airplane.query.get_or_404(airplane_type_id)

        db.session.delete(airplane_type)
        db.session.commit()
        return '', 204


# ------------------------------------------------
#                      Flight
# ------------------------------------------------

class FlightResource(Resource):
    def get(self, flight_id):
        flight = Flight.query.get_or_404(flight_id)
        return flight_schema.dump(flight)


class FlightListResource(Resource):
    def get(self):
        flights = Flight.query.all()
        return flights_schema.dump(flights)


class FlightCreationResource(Resource):
    def post(self):
        new_flight = Flight(
            id=request.json['flight_id'],
            route_id=request.json['route_id'],
            airplane_id=request.json['airplane_id'],
            departure_time=request.json['departure_time'],
            reserved_seats=request.json['reserved_seats'],
            seat_price=request.json['seat_price']
        )
        db.session.add(new_flight)
        db.session.commit()
        return flight_schema.dump(new_flight)


class FlightPatchResource(Resource):
    def post(self, flight_id):
        flight = Flight.query.get_or_404(flight_id)

        if 'flight_id' in request.json:
            flight.id = request.json['flight_id']
        if 'route_id' in request.json:
            flight.route_id = request.json['route_id']
        if 'airplane_id' in request.json:
            flight.airplane_id = request.json['airplane_id']
        if 'departure_time' in request.json:
            flight.departure_time = request.json['departure_time']
        if 'reserved_seats' in request.json:
            flight.reserved_seats = request.json['reserved_seats']
        if 'seat_price' in request.json:
            flight.seat_price = request.json['seat_price']

        db.session.commit()
        return flight_schema.dump(flight)


class FlightDeleteResource(Resource):
    def post(self, flight_id):
        flight = Flight.query.get_or_404(flight_id)

        db.session.delete(flight)
        db.session.commit()
        return '', 204


# ------------------------------------------------
#                      Route
# ------------------------------------------------

class RouteResource(Resource):
    def get(self, route_id):
        route = Route.query.get_or_404(route_id)
        return route_schema.dump(route)


class RouteListResource(Resource):
    def get(self):
        routes = Route.query.all()
        return routes_schema.dump(routes)


class RouteCreationResource(Resource):
    def post(self):
        new_route = Route(
            origin_id=request.json['origin_id'],
            destination_id=request.json['destination_id'],
            duration=request.json['duration']
        )
        db.session.add(new_route)
        db.session.commit()
        return route_schema.dump(new_route)


class RoutePatchResource(Resource):
    def post(self, route_id):
        route = Route.query.get_or_404(route_id)

        if 'route_id' in request.json:
            route.id = request.json['route_id']
        if 'origin_id' in request.json:
            route.origin_id = request.json['origin_id']
        if 'destination_id' in request.json:
            route.destination_id = request.json['destination_id']
        if 'duration' in request.json:
            route.duration = request.json['duration']

        db.session.commit()
        return route_schema.dump(route)


class RouteDeleteResource(Resource):
    def post(self, route_id):
        route = Route.query.get_or_404(route_id)

        db.session.delete(route)
        db.session.commit()
        return '', 204


# ######################################################################################################################
# ########################################                               ###############################################
# ########################################         Restful Routes        ###############################################
# ########################################                               ###############################################
# ######################################################################################################################

api = Api()


# ------------------------------------------------
#                   Airplane
# ------------------------------------------------

api.add_resource(AirplaneResource, '/api/v1/airplanes/<int:airplane_id>')
api.add_resource(AirplaneListResource, '/api/v1/airplanes/')
api.add_resource(AirplaneCreationResource, '/api/v1/airplanes/create/')
api.add_resource(AirplanePatchResource, '/api/v1/airplanes/update/')
api.add_resource(AirplaneDeleteResource, '/api/v1/airplanes/delete/')

# ------------------------------------------------
#                 Airplane Type
# ------------------------------------------------

api.add_resource(AirplaneTypeResource, '/api/v1/airplane_types/<int:airplane_type_id>')
api.add_resource(AirplaneTypeListResource, '/api/v1/airplane_types/')
api.add_resource(AirplaneTypeCreationResource, '/api/v1/airplane_types/create/')
api.add_resource(AirplaneTypePatchResource, '/api/v1/airplane_types/update/')
api.add_resource(AirplaneTypeDeleteResource, '/api/v1/airplane_types/delete/')


# ------------------------------------------------
#                   Airports
# ------------------------------------------------

api.add_resource(AirportResource, '/api/v1/airports/<iata_id>')
api.add_resource(AirportListResource, '/api/v1/airports/')
api.add_resource(AirportCreationResource, '/api/v1/airports/create/')
api.add_resource(AirportPatchResource, '/api/v1/airports/update/')
api.add_resource(AirportDeleteResource, '/api/v1/airports/delete/')


# ------------------------------------------------
#                      Flight
# ------------------------------------------------

api.add_resource(FlightResource, '/api/v1/flights/<int:flight_id>')
api.add_resource(FlightListResource, '/api/v1/flights/all/')
api.add_resource(FlightCreationResource, '/api/v1/flights/create/')
api.add_resource(FlightPatchResource, '/api/v1/flights/update/')
api.add_resource(FlightDeleteResource, '/api/v1/flights/delete/')


# ------------------------------------------------
#                      Route
# ------------------------------------------------

api.add_resource(RouteResource, '/api/v1/routes/<int:route_id>')
api.add_resource(RouteListResource, '/api/v1/routes/')
api.add_resource(RouteCreationResource, '/api/v1/routes/create/')
api.add_resource(RoutePatchResource, '/api/v1/routes/update/')
api.add_resource(RouteDeleteResource, '/api/v1/routes/delete/')
