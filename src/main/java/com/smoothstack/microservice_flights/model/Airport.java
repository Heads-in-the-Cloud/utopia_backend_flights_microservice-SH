package com.smoothstack.microservice_flights.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "airport")
public class Airport {

    @Id
    @Column(name = "iata_id")
    private String iata_id;

    @Column(name = "city")
    private String city;




    public Airport() {};

    public Airport(String iata_ID, String city) {
        this.iata_id = iata_ID;
        this.city = city;
    }

    @Override
    public String toString() {
        return String.format("%s --> %s", iata_id, city);
    }

    public String getIata_id() {
        return iata_id;
    }

    public void setIata_id(String iata_id) {
        this.iata_id = iata_id;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
}
