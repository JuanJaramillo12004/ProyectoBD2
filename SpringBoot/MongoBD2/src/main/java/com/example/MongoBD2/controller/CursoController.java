package com.example.MongoBD2.controller;

import com.example.MongoBD2.exception.CamposInvalidosException;
import com.example.MongoBD2.exception.RecursoNoEncontradoException;
import com.example.MongoBD2.model.CursoModel;
import com.example.MongoBD2.service.CursoService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import java.util.List;

@RestController
@RequestMapping("/apiweb/curso")
@CrossOrigin
public class CursoController {
    @Autowired
    private CursoService cursoService;

    //Crear un curso
    @PostMapping("/")
    public ResponseEntity<String> crearCurso(@RequestBody CursoModel curso) {
        cursoService.crearCurso(curso);
        return new ResponseEntity<String>(cursoService.crearCurso(curso), HttpStatus.OK);
    }

    //Listar Cursos
    @GetMapping("/")
    public ResponseEntity<List<CursoModel>> listarCursos() {
        List<CursoModel> cursos = cursoService.listarCursos();
        return new ResponseEntity<>(cursos, HttpStatus.OK);
    }

    //Consultar un curso por Id
    @GetMapping("/{cursoId}")
    public ResponseEntity<CursoModel> cursoPorId(@PathVariable Integer cursoId) {
        CursoModel curso = this.cursoService.cursoPorId(cursoId)
                .orElseThrow(() -> new RecursoNoEncontradoException("Error! No se encontró el curso con el id " + cursoId));
        return ResponseEntity.ok(curso);
    }

    //Actualizar la información básica del curso
    @PutMapping("/{cursoId}")
    public ResponseEntity<String> actualizarCursoPorId(@PathVariable Integer cursoId, @RequestBody CursoModel cursoData) {
        CursoModel curso = this.cursoService.cursoPorId(cursoId)
                .orElseThrow(() -> new RecursoNoEncontradoException("Error!. No se encontró el curso con el id " + cursoId));
        String actualizarNombre = cursoData.getNombre();
        String actualizarCategoria = cursoData.getCategoria();

        if (actualizarNombre != null && !actualizarNombre.isEmpty() && actualizarCategoria != null && !actualizarCategoria.isEmpty()) {
            curso.setNombre(actualizarNombre);
            curso.setCategoria(actualizarCategoria);
            return new ResponseEntity<String>(cursoService.actualizarCursoPorId(curso), HttpStatus.OK);
        } else {
            throw new CamposInvalidosException("Error!");
        }
    }
}


