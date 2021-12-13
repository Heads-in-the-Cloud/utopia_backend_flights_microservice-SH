package com.smoothstack.microservice_flights.service;

import com.smoothstack.microservice_flights.dao.AirplaneTypeDAO;
import com.smoothstack.microservice_flights.model.AirplaneType;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AirplaneTypeService {

    @Autowired
    private AirplaneTypeDAO airplaneTypeDao;

    public AirplaneType getByTypeId(int type_id) {
        try {
            return airplaneTypeDao.findById(type_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new AirplaneType();
    }

    public List<AirplaneType> getAllTypes() {
        return airplaneTypeDao.findAll();
    }

    public boolean insert(AirplaneType airplane_type) {
        try {
            airplaneTypeDao.save(airplane_type);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean delete(AirplaneType airplane_type) {
        try {
            airplaneTypeDao.delete(airplane_type);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean delete(int type_id) {
        try {
            airplaneTypeDao.deleteById(type_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
