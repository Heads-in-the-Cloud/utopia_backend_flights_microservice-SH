package com.smoothstack.microservice_flights.service;

import com.smoothstack.microservice_flights.dao.AirplaneDAO;
import com.smoothstack.microservice_flights.model.Airplane;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class AirplaneService {

    @Autowired
    private AirplaneDAO airplaneDao;

    public Airplane getById(int airplane_id) {
        try {
            return airplaneDao.findById(airplane_id).get();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return new Airplane();
    }

    public List<Airplane> getAll() {
        return airplaneDao.findAll();
    }

    public boolean upload(Airplane airplane) {
        try {
            airplaneDao.save(airplane);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean delete(Airplane airplane) {
        try {
            airplaneDao.delete(airplane);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean delete(int airplane_id) {
        try {
            airplaneDao.deleteById(airplane_id);
            return true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    }
}
