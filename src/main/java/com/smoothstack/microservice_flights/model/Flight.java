package com.smoothstack.microservice_flights.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.time.LocalDateTime;

@Entity
@Table(name = "flight")
public class Flight {

    @Id
    @Column(name = "id")
    private Integer id;

    @Column(name = "route_id")
    private Integer route_id;

    @Column(name = "airplane_id")
    private Integer airplane_id;

    @Column(name = "departure_time")
    private LocalDateTime departure_time;

    @Column(name = "reserved_seats")
    private Integer reserved_seats;

    @Column(name = "seat_price")
    private Float seat_price;




    public Flight() {};

    public Flight(Integer route_id, Integer airplane_id, LocalDateTime departure_time,
                  Integer reserved_seats, Float seat_price) {
        this.route_id = route_id;
        this.airplane_id = airplane_id;
        this.departure_time = departure_time;
        this.reserved_seats = reserved_seats;
        this.seat_price = seat_price;
    }

    public Flight(Integer ID, Integer route_id, Integer airplane_id, LocalDateTime departure_time,
                  Integer reserved_seats, Float seat_price) {
        this.id = ID;
        this.route_id = route_id;
        this.airplane_id = airplane_id;
        this.departure_time = departure_time;
        this.reserved_seats = reserved_seats;
        this.seat_price = seat_price;
    }

//    public Flight(FlightInfo flight) {
//        this.id = flight.flight_id();
//        this.route_id = flight.route_id();
//        this.airplane_id = flight.airplane_id();
//        this.departure_time = flight.departure_time();
//        this.reserved_seats = flight.reserved_seats();
//        this.seat_price = flight.seat_price();
//    }


    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getRoute_id() {
        return route_id;
    }

    public void setRoute_id(Integer route_id) {
        this.route_id = route_id;
    }

    public Integer getAirplane_id() {
        return airplane_id;
    }

    public void setAirplane_id(Integer airplane_id) {
        this.airplane_id = airplane_id;
    }

    public LocalDateTime getDeparture_time() {
        return departure_time;
    }

    public void setDeparture_time(LocalDateTime departure_time) {
        this.departure_time = departure_time;
    }

    public Integer getReserved_seats() {
        return reserved_seats;
    }

    public void setReserved_seats(Integer reserved_seats) {
        this.reserved_seats = reserved_seats;
    }

    public Float getSeat_price() {
        return seat_price;
    }

    public void setSeat_price(Float seat_price) {
        this.seat_price = seat_price;
    }
}
