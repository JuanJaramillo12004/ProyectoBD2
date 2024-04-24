package com.example.MongoBD2.repository;

import com.example.MongoBD2.model.UsuarioModel;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface UsuarioRepository extends MongoRepository<UsuarioModel, Integer> {
}
