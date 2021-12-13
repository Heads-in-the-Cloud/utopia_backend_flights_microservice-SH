package com.smoothstack.microservice_flights.dao;

import com.smoothstack.microservice_flights.model.Flight;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FlightDAO extends JpaRepository<Flight, Integer> {

}
