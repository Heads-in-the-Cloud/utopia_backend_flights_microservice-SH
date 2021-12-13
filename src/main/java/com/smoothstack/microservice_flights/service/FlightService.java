package com.smoothstack.microservice_flights.service;

import com.smoothstack.microservice_flights.dao.FlightDAO;
import com.smoothstack.microservice_flights.model.Flight;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class FlightService {

    @Autowired
    FlightDAO flightDao;

    public Flight getById(int flight_id) {
        try {
            return flightDao.findById(flight_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new Flight();
    }

    public List<Flight> getAllFlights() {
        return flightDao.findAll();
    }

    public boolean insertFlight(Flight flight) {
        try {
            flightDao.save(flight);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteFlight(Flight flight) {
        try {
            flightDao.delete(flight);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteFlight(int flight_id) {
        try {
            flightDao.deleteById(flight_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
