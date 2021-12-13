package com.smoothstack.microservice_flights.dao;

import com.smoothstack.microservice_flights.model.Route;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface RouteDAO extends JpaRepository<Route, Integer> {

}
