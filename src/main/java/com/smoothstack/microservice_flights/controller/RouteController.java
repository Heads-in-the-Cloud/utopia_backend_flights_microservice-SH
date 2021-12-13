package com.smoothstack.microservice_flights.controller;

import com.smoothstack.microservice_flights.model.Route;
import com.smoothstack.microservice_flights.service.RouteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/route")
public class RouteController {

    @Autowired
    private RouteService routeService;

    @GetMapping(path = "/{route_id}")
    public Route getById(@PathVariable int route_id) {
        return routeService.getById(route_id);
    }

    @GetMapping(path = "/all")
    public List<Route> getAllTypes() {
        return routeService.getAllRoutes();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody Route route) {
        return routeService.insertRoute(route);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody Route route) {
        return routeService.deleteRoute(route);
    }

    @PostMapping(path = "/delete/{route_id}")
    public boolean delete(@PathVariable int route_id) {
        return routeService.deleteRoute(route_id);
    }
}
