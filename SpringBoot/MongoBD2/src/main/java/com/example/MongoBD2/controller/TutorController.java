package com.example.MongoBD2.controller;

import com.example.MongoBD2.exception.CamposInvalidosException;
import com.example.MongoBD2.exception.RecursoNoEncontradoException;
import com.example.MongoBD2.model.CursoModel;
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

    //Crear un tutor
    @PostMapping("/")
    public ResponseEntity<String> crearTutor(@RequestBody TutorModel tutor) {
        tutorService.crearTutor(tutor);
        return new ResponseEntity<String>(tutorService.crearTutor(tutor), HttpStatus.OK);
    }
    //Listar tutores
    @GetMapping("/")
    public ResponseEntity<List<TutorModel>> listarTutores() {
        List<TutorModel> tutores = tutorService.listarTutores();
        return new ResponseEntity<>(tutores, HttpStatus.OK);
    }
    //Consultar un tutor por Id
    @GetMapping("/{tutorId}")
    public ResponseEntity<TutorModel> tutorPorId(@PathVariable Integer tutorId) {
        TutorModel tutor = this.tutorService.tutorPorId(tutorId)
                .orElseThrow(() -> new RecursoNoEncontradoException("Error! No se encontró el curso con el id " + tutorId));
        return ResponseEntity.ok(tutor);
    }

    //Actualizar la información básica del curso
    @PutMapping("/{tutorId}")
    public ResponseEntity<String> actualizarTutorPorId(@PathVariable Integer tutorId, @RequestBody TutorModel tutorData) {
        TutorModel tutor = this.tutorService.tutorPorId(tutorId)
                .orElseThrow(() -> new RecursoNoEncontradoException("Error!. No se encontró el tutor con el id " + tutorId));
        String actualizarNombre = tutorData.getNombre();
        String actualizarFacultad = tutorData.getFacultad();

        if (actualizarNombre != null && !actualizarNombre.isEmpty() && actualizarFacultad != null && !actualizarFacultad.isEmpty()) {
            tutor.setNombre(actualizarNombre);
            tutor.setFacultad(actualizarFacultad);
            return new ResponseEntity<String>(tutorService.actualizarTutorPorId(tutor), HttpStatus.OK);
        } else {
            throw new CamposInvalidosException("Error!");
        }
    }
}
