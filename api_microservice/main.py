# ######################################################################################################################
# ########################################                               ###############################################
# ########################################              Main             ###############################################
# ########################################                               ###############################################
# ######################################################################################################################

from typing import List

from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

from .haversine import Haversine
from .database import engine
from . import (
    models as m,
    schemas as s
)

m.Base.metadata.create_all(bind=engine)

app = FastAPI()


# ######################################################################################################################
# ########################################                               ###############################################
# ########################################          API Routes           ###############################################
# ########################################                               ###############################################
# ######################################################################################################################


@app.get("/health")
def health_check():
    return "Healthy"


# ------------------------------------------------
#                   Airplane
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/airplanes/", response_model=s.AirplaneFull)
def create_airplane(airplane: s.Airplane):
    with Session(engine) as db:
        db_airplane = m.Airplane(type_id=airplane.type_id)

        db.add(db_airplane)
        db.commit()
        db.refresh(db_airplane)

        return db_airplane


# --------------------   Read   ------------------


@app.get("/api/v2/airplanes/{airplane_id}", response_model=s.AirplaneFull)
def get_airplane(airplane_id: int):
    with Session(engine) as db:
        db_airplane = db                                \
            .query(m.Airplane)                          \
            .filter(m.Airplane.id == airplane_id)       \
            .first()

        if not db_airplane:
            raise HTTPException(
                status_code=404,
                detail="Airplane not found"
            )

        return db_airplane


@app.get("/api/v2/airplanes/", response_model=List[s.AirplaneFull])
def get_airplanes():
    with Session(engine) as db:
        airplanes = db              \
            .query(m.Airplane)      \
            .all()

        if not airplanes:
            raise HTTPException(
                status_code=404,
                detail="No airplanes found"
            )

        return airplanes


@app.get("/api/v2/airplanes/type={type_id}", response_model=List[s.AirplaneFull])
def get_airplanes_with_type(type_id: int):
    with Session(engine) as db:
        type_airplanes = db                             \
            .query(m.Airplane)                          \
            .filter(m.Airplane.type_id == type_id)      \
            .all()

        if not type_airplanes:
            raise HTTPException(
                status_code=404,
                detail="No airplanes found"
            )

        return type_airplanes


# --------------------  Update  ------------------


@app.patch("/api/v2/airplanes/{airplane_id}", response_model=s.AirplaneFull)
def update_plane(airplane_id: int, airplane: s.AirplaneUpdate):
    with Session(engine) as db:
        db_airplane = db                                \
            .query(m.Airplane)                          \
            .filter(m.Airplane.id == airplane_id)       \
            .first()

        if not db_airplane:
            raise HTTPException(
                status_code=404,
                detail="Airplane not found"
            )

        airplane_data = airplane.dict(exclude_unset=True)
        for key, value in airplane_data.items():
            setattr(db_airplane, key, value)

        db.add(db_airplane)
        db.commit()
        db.refresh(db_airplane)

        return db_airplane


# --------------------  Delete  ------------------


@app.delete("/api/v2/airplanes/{airplane_id}")
def delete_airplane(airplane_id: int):
    with Session(engine) as db:
        db_airplane = db                                \
            .query(m.Airplane)                          \
            .filter(m.Airplane.id == airplane_id)       \
            .first()

        if not db_airplane:
            raise HTTPException(
                status_code=404,
                detail="Airplane not found"
            )

        db.delete(db_airplane)
        db.commit()

        return {"ok": True}


# ------------------------------------------------
#                 Airplane Type
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/airplane_types/", response_model=s.AirplaneTypeFull)
def create_airplane_type(plane_type: s.AirplaneType):
    with Session(engine) as db:
        new_type = m.AirplaneType(
            max_capacity=plane_type.max_capacity
        )

        db.add(new_type)
        db.commit()
        db.refresh(new_type)

        return new_type


# --------------------   Read   ------------------


@app.get("/api/v2/airplane_types/{type_id}", response_model=s.AirplaneTypeFull)
def get_airplane_type(type_id: int):
    with Session(engine) as db:
        db_type = db                                    \
            .query(m.AirplaneType)                      \
            .filter(m.AirplaneType.id == type_id)       \
            .first()

        if not db_type:
            raise HTTPException(
                status_code=404,
                detail="Airplane type not found"
            )

        return db_type


@app.get("/api/v2/airplane_types/capacity={desired_capacity}", response_model=s.AirplaneTypeFull)
def get_airplane_type_capacity_gt(desired_capacity: int):
    with Session(engine) as db:
        db_type = db                                                    \
            .query(m.AirplaneType)                                      \
            .filter(m.AirplaneType.max_capacity >= desired_capacity)    \
            .first()

        if not db_type:
            raise HTTPException(
                status_code=404,
                detail="No suitable airplane type not found"
            )

        return db_type


@app.get("/api/v2/airplane_types/", response_model=List[s.AirplaneTypeFull])
def get_airplane_types():
    with Session(engine) as db:
        types = db                      \
            .query(m.AirplaneType)      \
            .all()

        if not types:
            raise HTTPException(
                status_code=404,
                detail="No airplane types not found"
            )


# --------------------  Update  ------------------


@app.patch("/api/v2/airplane_types/{type_id}", response_model=s.AirplaneTypeFull)
def update_airplane_type(type_id: int, update_type: s.AirplaneTypeUpdate):
    with Session(engine) as db:
        db_type = db                                    \
            .query(m.AirplaneType)                      \
            .filter(m.AirplaneType.id == type_id)       \
            .first()

        if not db_type:
            raise HTTPException(
                status_code=404,
                detail="Airplane type not found"
            )

        type_data = update_type.dict(exclude_unset=True)
        for key, value in type_data.items():
            setattr(db_type, key, value)

        db.add(db_type)
        db.commit()
        db.refresh(db_type)

        return db_type


# --------------------  Delete  ------------------


@app.delete("/api/v2/airplane_types/{type_id}")
def delete_airplane_type(type_id: int):
    with Session(engine) as db:
        db_type = db                                    \
            .query(m.AirplaneType)                      \
            .filter(m.AirplaneType.id == type_id)       \
            .first()

        if not db_type:
            raise HTTPException(
                status_code=404,
                detail="Airplane type not found"
            )

        affected_planes = get_airplanes_with_type(type_id)
        for plane in affected_planes:
            delete_airplane(plane.id, db)

        db.delete(db_type)
        db.commit()

        return {"ok": True}


# ------------------------------------------------
#                   Airports
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/airports/", response_model=s.Airport)
def create_airport(airport: s.Airport):
    with Session(engine) as db:
        db_airport = db                                     \
            .query(m.Airport)                               \
            .filter(m.Airport.iata_id == airport.iata_id)   \
            .first()

        if db_airport:
            raise HTTPException(
                status_code=400,
                detail="Airport with that iata_id already exists"
            )

        new_airport = m.Airport(
            iata_id=airport.iata_id,
            city=airport.city,
            name=airport.name,
            longitude=airport.longitude,
            latitude=airport.latitude,
            elevation=airport.elevation
        )

        db.add(new_airport)
        db.commit()
        db.refresh(new_airport)

        return new_airport


# --------------------   Read   ------------------


@app.get("/api/v2/airports/{iata_id}", response_model=s.Airport)
def get_airport(iata_id: str):
    with Session(engine) as db:
        db_airport = db                                 \
            .query(m.Airport)                           \
            .filter(m.Airport.iata_id == iata_id)       \
            .first()

        if not db_airport:
            raise HTTPException(
                status_code=404,
                detail="Airport not found"
            )

        return db_airport


@app.get("/api/v2/airports/city={city}", response_model=s.Airport)
def get_airports_by_city(city: str):
    with Session(engine) as db:
        city_airports = db                      \
            .query(m.Airport)                   \
            .filter(m.Airport.city == city)     \
            .all()

        if not city_airports:
            raise HTTPException(
                status_code=404,
                detail="No airports found for city"
            )

        return city_airports


@app.get("/api/v2/airports/", response_model=List[s.Airport])
def get_airports():
    with Session(engine) as db:
        airports = db               \
            .query(m.Airport)       \
            .all()

        if not airports:
            raise HTTPException(
                status_code=404,
                detail="No airports found"
            )

        return airports


# --------------------  Update  ------------------


@app.patch("/api/v2/airports/{iata_id}", response_model=s.Airport)
def update_airport(iata_id: str, airport: s.AirportUpdate):
    with Session(engine) as db:
        db_airport = db                                 \
            .query(m.Airport)                           \
            .filter(m.Airport.iata_id == iata_id)       \
            .first()

        if not db_airport:
            raise HTTPException(
                status_code=404,
                detail="Airport not found"
            )

        airport_data = airport.dict(exclude_unset=True)
        for key, value in airport_data.items():
            setattr(db_airport, key, value)

        db.add(db_airport)
        db.commit()
        db.refresh(db_airport)

        return db_airport


# --------------------  Delete  ------------------


@app.delete("/api/v2/airports/{iata_id}")
def delete_airport(iata_id: str):
    with Session(engine) as db:
        db_airport = db                                 \
            .query(m.Airport)                           \
            .filter(m.Airport.iata_id == iata_id)       \
            .first()

        if not db_airport:
            raise HTTPException(
                status_code=404,
                detail="Airport not found"
            )

        affected_routes = db                                    \
            .query(m.Route)                                     \
            .filter(m.Route.origin_id == iata_id or
                    m.Route.destination_id == iata_id)          \
            .all()

        for route in affected_routes:
            delete_route(route.id)

        db.delete(db_airport)
        db.commit()

        return {"ok": True}


# ------------------------------------------------
#                      Flight
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/flights/", response_model=s.FlightFull)
def create_flight(flight: s.Flight):
    with Session(engine) as db:
        db_flight = db                          \
            .query(m.Flight)                    \
            .fliter(m.Flight == flight)         \
            .first()

        if db_flight:
            raise HTTPException(
                status_code=400,
                detail="Flight already exists"
            )

        new_flight = m.Flight(
            route_id=flight.route_id,
            airplane_id=flight.airplane_id,
            departure_time=flight.departure_time,
            reserved_seats=flight.reserved_seats,
            seat_price=flight.seat_price
        )

        db.add(new_flight)
        db.commit()
        db.refresh(new_flight)

        return new_flight


# --------------------   Read   ------------------


@app.get("/api/v2/flights/{flight_id}", response_model=s.FlightFull)
def get_flight(flight_id: int):
    with Session(engine) as db:
        db_flight = db                              \
            .query(m.Flight)                        \
            .fliter(m.Flight.id == flight_id)       \
            .first()

        if not db_flight:
            raise HTTPException(
                status_code=404,
                detail="Flight not found"
            )

        return db_flight


@app.get("/api/v2/flights/", response_model=List[s.FlightFull])
def get_flights_by_route(route_id: int):
    with Session(engine) as db:
        flights = db                                  \
            .query(m.Flight)                            \
            .filter(m.Flight.route_id == route_id)      \
            .all()

        if not flights:
            raise HTTPException(
                status_code=404,
                detail="No flights found"
            )

        return flights


# --------------------  Update  ------------------


@app.patch("/api/v2/flights/{flight_id}", response_model=s.FlightFull)
def update_flight(flight_id: int, flight: s.FlightUpdate):
    with Session(engine) as db:
        db_flight = db                              \
            .query(m.Flight)                        \
            .fliter(m.Flight.id == flight_id)       \
            .first()

        if not db_flight:
            raise HTTPException(
                status_code=404,
                detail="Flight not found"
            )

        flight_data = flight.dict(exclude_unset=True)
        for key, value in flight_data.items():
            setattr(db_flight, key, value)

        db.add(db_flight)
        db.commit()
        db.refresh(db_flight)

        return db_flight


# --------------------  Delete  ------------------


@app.delete("/api/v2/flights/{flight_id}")
def delete_flight(flight_id: int):
    with Session(engine) as db:
        db_flight = db                              \
            .query(m.Flight)                        \
            .fliter(m.Flight.id == flight_id)       \
            .first()

        if not db_flight:
            raise HTTPException(
                status_code=404,
                detail="Flight not found"
            )

        db.delete(db_flight)
        db.commit()

        return {"ok": True}


# ------------------------------------------------
#                      Route
# ------------------------------------------------

# --------------------  Create  ------------------


@app.post("/api/v2/routes/", response_model=s.RouteFull)
def create_route(origin: s.Airport, destination: s.Airport):
    with Session(engine) as db:
        distance = Haversine(
            (origin.longitude, origin.latitude),
            (destination.longitude, destination.latitude)
        ).miles

        duration = distance / 500  # Average flight speed is roughly 500 mph

        new_route = m.Route(
            origin_id=origin.iata_id,
            destination_id=destination.iata_id,
            duration=duration
        )

        db.add(new_route)
        db.commit()
        db.refresh(new_route)

        return new_route


# --------------------   Read   ------------------


@app.get("/api/v2/routes/{route_id}", response_model=s.RouteFull)
def get_route(route_id: int):
    with Session(engine) as db:
        db_route = db                               \
            .query(m.Route)                         \
            .filter(m.Route.id == route_id)         \
            .first()

        if not db_route:
            raise HTTPException(
                status_code=404,
                detail="Route not found"
            )

        return db_route


@app.get("/api/v2/routes/", response_model=List[s.RouteFull])
def get_routes():
    with Session(engine) as db:
        routes = db                 \
            .query(m.Route)         \
            .all()

        if not routes:
            raise HTTPException(
                status_code=404,
                detail="No routes found"
            )

        return routes


@app.get("/api/v2/routes/origin={iata_id}", response_model=List[s.RouteFull])
def get_routes_by_origin(iata_id: str):
    with Session(engine) as db:
        routes = db                                     \
            .query(m.Route)                             \
            .filter(m.Route.origin_id == iata_id)       \
            .all()

        if not routes:
            raise HTTPException(
                status_code=404,
                detail="No routes found"
            )

        return routes


@app.get("/api/v2/routes/destination={iata_id}", response_model=List[s.RouteFull])
def get_routes_by_destination(iata_id: str):
    with Session(engine) as db:
        routes = db                                         \
            .query(m.Route)                                 \
            .filter(m.Route.destination_id == iata_id)      \
            .all()

        if not routes:
            raise HTTPException(
                status_code=404,
                detail="No routes found"
            )

        return routes


@app.get("/api/v2/routes/duration={duration}", response_model=List[s.RouteFull])
def get_routes_by_duration(duration: int):
    with Session(engine) as db:
        routes = db                                   \
            .query(m.Route)                         \
            .filter(m.Route.duration == duration)   \
            .all()

        if not routes:
            raise HTTPException(
                status_code=404,
                detail="No routes found"
            )

        return routes


# --------------------  Update  ------------------


@app.patch("/api/v2/routes/{route_id}", response_model=s.RouteFull)
def update_route(route_id: int, route: s.RouteUpdate):
    with Session(engine) as db:
        db_route = db                               \
            .query(m.Route)                         \
            .filter(m.Route.id == route_id)         \
            .first()

        if not db_route:
            raise HTTPException(
                status_code=404,
                detail="Route not found"
            )

        route_data = route.dict(exclude_unset=True)
        for key, value in route_data.items():
            setattr(db_route, key, value)

        db.add(db_route)
        db.commit()
        db.refresh(db_route)

        return db_route


# --------------------  Delete  ------------------


@app.delete("/api/v2/routes/{route_id}")
def delete_route(route_id: int):
    with Session(engine) as db:
        db_route = db                               \
            .query(m.Route)                         \
            .filter(m.Route.id == route_id)         \
            .first()

        if not db_route:
            raise HTTPException(
                status_code=404,
                detail="Route not found"
            )

        affected_flights = db                           \
            .query(m.Flight)                            \
            .filter(m.Flight.route_id == route_id)      \
            .all()

        for flight in affected_flights:
            delete_flight(db, flight.id)

        db.delete(db_route)
        db.commit()

        return {"ok": True}
