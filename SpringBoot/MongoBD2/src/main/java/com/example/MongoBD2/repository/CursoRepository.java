package com.example.MongoBD2.repository;

import com.example.MongoBD2.model.CursoModel;
import org.springframework.data.mongodb.repository.Aggregation;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CursoRepository extends MongoRepository<CursoModel, Integer>{

}
