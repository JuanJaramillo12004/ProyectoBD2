package com.example.MongoBD2.service;

import com.example.MongoBD2.model.TutorModel;
import java.util.List;
import java.util.Optional;

public interface TutorService {
    String crearTutor(TutorModel tutor);
    List<TutorModel> listarTutores();
    Optional<TutorModel> tutorPorId(int tutorid);
    String actualizarTutorPorId(TutorModel tutor);
    List<TutorModel> mostrarCalificacionesMayoresAN(double calificacion);
}
