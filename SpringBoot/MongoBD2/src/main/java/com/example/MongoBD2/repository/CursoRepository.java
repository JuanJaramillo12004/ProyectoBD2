package com.example.MongoBD2.repository;

import com.example.MongoBD2.model.CursoModel;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface CursoRepository extends MongoRepository<CursoModel, Integer>{
}
