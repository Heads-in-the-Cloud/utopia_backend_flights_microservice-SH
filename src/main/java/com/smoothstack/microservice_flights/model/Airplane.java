package com.smoothstack.microservice_flights.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "airplane")
public class Airplane {

    @Id
    @Column(name = "id")
    public Integer id;

    @Column(name = "type_id")
    public Integer type_id;




    public Airplane() {};

    public Airplane(Integer ID, Integer type) {
        this.id = ID;
        this.type_id = type;
    }

    public String toString() {
        return String.format("Plane %d --> type %d", this.id, this.type_id);
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public Integer getType_id() {
        return type_id;
    }

    public void setType_id(Integer type_id) {
        this.type_id = type_id;
    }
}
