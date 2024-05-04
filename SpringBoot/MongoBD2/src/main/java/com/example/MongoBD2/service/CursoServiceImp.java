package com.example.MongoBD2.service;

import com.example.MongoBD2.model.CursoModel;
import com.example.MongoBD2.repository.CursoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@Primary

public class CursoServiceImp implements CursoService{
    @Autowired
    CursoRepository cursoRepository;

    @Override
    public String crearCurso(CursoModel curso){
        this.cursoRepository.save(curso);
        return "Curso " + curso.getNombre() + " creado";
    }

    @Override
    public List<CursoModel> listarCursos(){
        return this.cursoRepository.findAll();
    }

    @Override
    public Optional<CursoModel> cursoPorId(int cursoid){
        return this.cursoRepository.findById(cursoid);
    }

    @Override
    public String actualizarCursoPorId(CursoModel curso){
        this.cursoRepository.save(curso);
        return "Curso " + curso.getNombre() + " actualizado";
    }

    @Override
    public List<CursoModel> mostrarCursosPorCalificacion(double calificacion){
        return this.cursoRepository.listarCursosCalificacionesMayoresAN(calificacion);
    }
}
