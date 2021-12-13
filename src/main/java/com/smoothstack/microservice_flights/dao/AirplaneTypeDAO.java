package com.smoothstack.microservice_flights.dao;

import com.smoothstack.microservice_flights.model.AirplaneType;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AirplaneTypeDAO extends JpaRepository<AirplaneType, Integer> {

}