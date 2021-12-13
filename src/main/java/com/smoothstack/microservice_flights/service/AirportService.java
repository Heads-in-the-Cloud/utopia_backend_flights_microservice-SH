package com.smoothstack.microservice_flights.service;

import com.smoothstack.microservice_flights.dao.AirportDAO;
import com.smoothstack.microservice_flights.model.Airport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AirportService {

    @Autowired
    private AirportDAO airportDao;

    public Airport getByIataId(String iata_id) {
        try {
            return airportDao.findById(iata_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new Airport();
    }

    public List<Airport> getAllTypes() {
        return airportDao.findAll();
    }

    public boolean insertAirport(Airport airport) {
        try {
            airportDao.save(airport);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteAirport(Airport airport) {
        try {
            airportDao.delete(airport);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean deleteAirport(String iata_id) {
        try {
            airportDao.deleteById(iata_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
