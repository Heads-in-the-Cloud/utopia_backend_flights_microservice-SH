package com.smoothstack.microservice_flights.controller;

import com.smoothstack.microservice_flights.model.Airport;
import com.smoothstack.microservice_flights.service.AirportService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/airport")
public class AirportController {

    @Autowired
    private AirportService airportService;

    @GetMapping(path = "/{iata_id}")
    public Airport getByIataId(@PathVariable String iata_id) {
        return airportService.getByIataId(iata_id);
    }

    @GetMapping(path = "/all")
    public List<Airport> getAllTypes() {
        return airportService.getAllTypes();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody Airport airport) {
        return airportService.insertAirport(airport);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody Airport airport) {
        return airportService.deleteAirport(airport);
    }

    @PostMapping(path = "/delete/{iata_id}")
    public boolean delete(@PathVariable String iata_id) {
        return airportService.deleteAirport(iata_id);
    }
}
