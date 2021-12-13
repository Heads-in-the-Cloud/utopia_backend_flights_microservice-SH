package com.smoothstack.microservice_flights.controller;

import com.smoothstack.microservice_flights.model.Flight;
import com.smoothstack.microservice_flights.service.FlightService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/flight")
public class FlightController {

    @Autowired
    private FlightService flightService;

    @GetMapping(path = "/{flight_id}")
    public Flight getById(@PathVariable int flight_id) {
        return flightService.getById(flight_id);
    }

    @GetMapping(path = "/all")
    public List<Flight> getAllTypes() {
        return flightService.getAllFlights();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody Flight flight) {
        return flightService.insertFlight(flight);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody Flight flight) {
        return flightService.deleteFlight(flight);
    }

    @PostMapping(path = "/delete/{flight_id}")
    public boolean delete(@PathVariable int flight_id) {
        return flightService.deleteFlight(flight_id);
    }

}
