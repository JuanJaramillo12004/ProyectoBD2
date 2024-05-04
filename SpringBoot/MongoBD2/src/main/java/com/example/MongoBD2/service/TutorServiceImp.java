package com.example.MongoBD2.service;

import com.example.MongoBD2.model.TutorModel;
import com.example.MongoBD2.repository.TutorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@Primary

public class TutorServiceImp implements TutorService{
    @Autowired
    TutorRepository tutorRepository;

    @Override
    public String crearTutor(TutorModel tutor){
        this.tutorRepository.save(tutor);
        return "Tutor " + tutor.getNombre() + " creado";
    }

    @Override
    public List<TutorModel> listarTutores(){
        return this.tutorRepository.findAll();
    }

    @Override
    public Optional<TutorModel> tutorPorId(int tutorid){
        return this.tutorRepository.findById(tutorid);
    }

    @Override
    public String actualizarTutorPorId(TutorModel tutor){
        this.tutorRepository.save(tutor);
        return "Tutor " + tutor.getNombre() + " actualizado";
    }

    @Override
    public List<TutorModel> mostrarCalificacionesMayoresAN(double calificacion){
        return this.tutorRepository.listarCalificacionesMayoresAN(calificacion);
    }
}
