package com.example.MongoBD2.controller;

import com.example.MongoBD2.exception.CamposInvalidosException;
import com.example.MongoBD2.exception.RecursoNoEncontradoException;
import com.example.MongoBD2.model.UsuarioModel;
import com.example.MongoBD2.service.UsuarioService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import java.util.List;

@RestController
@RequestMapping("/apiweb/usuario")
@CrossOrigin
public class UsuarioController {
    @Autowired
    private UsuarioService usuarioService;

    //Crear un curso
    @PostMapping("/")
    public ResponseEntity<String> crearTutor(@RequestBody UsuarioModel usuario) {
        usuarioService.crearUsuario(usuario);
        return new ResponseEntity<String>(usuarioService.crearUsuario(usuario), HttpStatus.OK);
    }
    //Listar Cursos
    @GetMapping("/")
    public ResponseEntity<List<UsuarioModel>> listarUsuarios() {
        List<UsuarioModel> usuarios = usuarioService.listarUsuarios();
        return new ResponseEntity<>(usuarios, HttpStatus.OK);
    }
    //Consultar un curso por Id
    @GetMapping("/{tutorId}")
    public ResponseEntity<UsuarioModel> usuarioPorId(@PathVariable Integer usuarioId) {
        UsuarioModel usuario = this.usuarioService.usuarioPorId(usuarioId)
                .orElseThrow(() -> new RecursoNoEncontradoException("Error! No se encontró el curso con el id " + usuarioId));
        return ResponseEntity.ok(usuario);
    }
}
