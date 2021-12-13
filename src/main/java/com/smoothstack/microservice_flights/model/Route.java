package com.smoothstack.microservice_flights.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "route")
public class Route {

    @Id
    @Column(name = "id")
    Integer id;

    @Column(name = "origin_id")
    String origin_id;

    @Column(name = "destination_id")
    String destination_id;



    public Route() {};

    public Route(String orig, String dest) {
        this.origin_id = orig;
        this.destination_id = dest;
    }

    public Route(Integer ID, String orig, String dest) {
        this.id = ID;
        this.origin_id = orig;
        this.destination_id = dest;
    }

    public String toString() {
        return String.format("Route ID: %d\t| Origin: %s --> Destination: %s",
                this.id, this.origin_id, this.destination_id);
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getOrigin_id() {
        return origin_id;
    }

    public void setOrigin_id(String origin_id) {
        this.origin_id = origin_id;
    }

    public String getDestination_id() {
        return destination_id;
    }

    public void setDestination_id(String destination_id) {
        this.destination_id = destination_id;
    }
}
