package com.example.MongoBD2.service;

import com.example.MongoBD2.model.CursoModel;
import java.util.List;
import java.util.Optional;

public interface CursoService {
    String crearCurso(CursoModel curso);
    List<CursoModel> listarCursos();
    Optional<CursoModel> cursoPorId(int cursoid);
    String actualizarCursoPorId(CursoModel curso);
    List<CursoModel> mostrarCursosPorCalificacionMayoresAN(double calificacion);
}
