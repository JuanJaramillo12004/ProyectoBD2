package com.example.MongoBD2.repository;

import com.example.MongoBD2.model.TutorModel;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface TutorRepository extends MongoRepository<TutorModel, Integer> {
}
