package com.smoothstack.microservice_flights.controller;

import com.smoothstack.microservice_flights.model.AirplaneType;
import com.smoothstack.microservice_flights.service.AirplaneTypeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/utopia/airplane_type")
public class AirplaneTypeController {

    @Autowired
    private AirplaneTypeService airplaneTypeService;

    @GetMapping(path = "/{type_id}")
    public AirplaneType getByTypeId(@PathVariable int type_id) {
        return airplaneTypeService.getByTypeId(type_id);
    }

    @GetMapping(path = "/all")
    public List<AirplaneType>  getAllTypes() {
        return airplaneTypeService.getAllTypes();
    }

    @PostMapping(path = "/upload")
    public boolean insertType(@RequestBody AirplaneType airplane_type) {
        return airplaneTypeService.insert(airplane_type);
    }

    @PostMapping(path = "/delete")
    public boolean delete(@RequestBody AirplaneType airplane_type) {
        return airplaneTypeService.delete(airplane_type);
    }
}
