package com.example.MongoBD2.repository;

import com.example.MongoBD2.model.CalificacionModel;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface CalificacionRepository extends MongoRepository<CalificacionModel, Integer> {
}
