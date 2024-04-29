package com.example.MongoBD2.controller;

import com.example.MongoBD2.exception.CamposInvalidosException;
import com.example.MongoBD2.exception.RecursoNoEncontradoException;
import com.example.MongoBD2.model.TutorModel;
import com.example.MongoBD2.service.TutorService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import java.util.List;

@RestController
@RequestMapping("/apiweb/tutor")
@CrossOrigin
public class TutorController {
    @Autowired
    private TutorService tutorService;

    //Crear un curso
    @PostMapping("/")
    public ResponseEntity<String> crearTutor(@RequestBody TutorModel tutor) {
        tutorService.crearTutor(tutor);
        return new ResponseEntity<String>(tutorService.crearTutor(tutor), HttpStatus.OK);
    }
    //Listar Cursos
    @GetMapping("/")
    public ResponseEntity<List<TutorModel>> listarTutores() {
        List<TutorModel> tutores = tutorService.listarTutores();
        return new ResponseEntity<>(tutores, HttpStatus.OK);
    }
    //Consultar un curso por Id
    @GetMapping("/{tutorId}")
    public ResponseEntity<TutorModel> tutorPorId(@PathVariable Integer tutorId) {
        TutorModel tutor = this.tutorService.tutorPorId(tutorId)
                .orElseThrow(() -> new RecursoNoEncontradoException("Error! No se encontró el curso con el id " + tutorId));
        return ResponseEntity.ok(tutor);
    }
}
