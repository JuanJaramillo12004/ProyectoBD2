package com.example.MongoBD2.repository;

import com.example.MongoBD2.model.TutorModel;
import org.springframework.data.mongodb.repository.Aggregation;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface TutorRepository extends MongoRepository<TutorModel, Integer> {
    @Aggregation({
            "{'$lookup': {'from': 'Cursos', 'localField': '_id', 'foreignField': 'tutorId', 'as': 'Cursos'}}",
            "{'$lookup': {'from': 'Calificaciones', 'localField': 'Cursos._id', 'foreignField': 'id_curso', 'as': 'Cursos.Calificaciones'}}",
            "{'$unwind': '$Cursos.Calificaciones'}",
            "{'$match': {'Cursos.Calificaciones.calificacion': {'$gte': ?0}}}",
            "{'$group': {'_id': {'_id': '$_id', 'nombre': '$nombre', 'facultad': '$facultad'}, 'Cursos': {'$push': '$Cursos'}}}",
            "{'$project': {'_id': '$_id._id', 'nombre': '$_id.nombre', 'facultad': '$_id.facultad', 'tutor': 1, 'Cursos': 1}}"})
    List<TutorModel> listarCalificacionesMayoresAN(Double calificacion);
}