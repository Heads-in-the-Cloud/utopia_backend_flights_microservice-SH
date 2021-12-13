package com.smoothstack.microservice_flights.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "airplane_type")
public class AirplaneType {

    @Id
    @Column(name = "id")
    private Integer id;

    @Column(name = "max_capacity")
    private Integer max_capacity;




    public AirplaneType() {};

    public AirplaneType(Integer ID, Integer max_cap) {
        this.id = ID;
        this.max_capacity = max_cap;
    }

    public String toString() {
        return String.format("Type %d --> Max Cap: %d", this.id, this.max_capacity);
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getMax_capacity() {
        return max_capacity;
    }

    public void setMax_capacity(Integer max_capacity) {
        this.max_capacity = max_capacity;
    }
}
