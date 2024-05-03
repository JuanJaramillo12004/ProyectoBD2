package com.example.MongoBD2.service;

import com.example.MongoBD2.model.CalificacionModel;
import java.util.List;
import java.util.Optional;

public interface CalificacionService {
    String crearCalificacion(CalificacionModel calificacion);
    List<CalificacionModel> listarCalificaciones();
    Optional<CalificacionModel> calificacionPorId(int calificacionid);
    String actualizarCalPorId(CalificacionModel calificacion);
}
