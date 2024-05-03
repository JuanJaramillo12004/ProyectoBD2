package com.example.MongoBD2.service;

import com.example.MongoBD2.model.CalificacionModel;
import com.example.MongoBD2.repository.CalificacionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@Primary

public class CalificacionServiceImp implements CalificacionService{
    @Autowired
    CalificacionRepository calificacionRepository;

    @Override
    public String crearCalificacion(CalificacionModel calificacion){
        this.calificacionRepository.save(calificacion);
        return "Calificacion creado";
    }

    @Override
    public List<CalificacionModel> listarCalificaciones(){
        return this.calificacionRepository.findAll();
    }

    @Override
    public Optional<CalificacionModel> calificacionPorId(int calificacionid){
        return this.calificacionRepository.findById(calificacionid);
    }

    @Override
    public String actualizarCalPorId(CalificacionModel calificacion){
        this.calificacionRepository.save(calificacion);
        return "Calificacion actualizado";
    }
}
