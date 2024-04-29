package com.example.MongoBD2.controller;

import com.example.MongoBD2.exception.CamposInvalidosException;
import com.example.MongoBD2.exception.RecursoNoEncontradoException;
import com.example.MongoBD2.model.CalificacionModel;
import com.example.MongoBD2.service.CalificacionService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import java.util.List;

@RestController
@RequestMapping("/apiweb/calificacion")
@CrossOrigin
public class CalificacionController {
    @Autowired
    private CalificacionService calificacionService;

    //Crear un calificacion
    @PostMapping("/")
    public ResponseEntity<String> crearCurso(@RequestBody CalificacionModel calificacion) {
        calificacionService.crearCalificacion(calificacion);
        return new ResponseEntity<String>(calificacionService.crearCalificacion(calificacion), HttpStatus.OK);
    }
    //Listar calificaciones
    @GetMapping("/")
    public ResponseEntity<List<CalificacionModel>> listarCalificaciones() {
        List<CalificacionModel> calificaciones = calificacionService.listarCalificaciones();
        return new ResponseEntity<>(calificaciones, HttpStatus.OK);
    }
    //Consultar un calificacion por Id
    @GetMapping("/{calificacionId}")
    public ResponseEntity<CalificacionModel> calificacionPorId(@PathVariable Integer calificacionId) {
        CalificacionModel calificacion = this.calificacionService.calificacionPorId(calificacionId)
                .orElseThrow(() -> new RecursoNoEncontradoException("Error! No se encontró el curso con el id " + calificacionId));
        return ResponseEntity.ok(calificacion);
    }
}
