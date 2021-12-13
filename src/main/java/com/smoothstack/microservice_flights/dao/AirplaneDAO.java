package com.smoothstack.microservice_flights.dao;

import com.smoothstack.microservice_flights.model.Airplane;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AirplaneDAO extends JpaRepository<Airplane, Integer> {

}
