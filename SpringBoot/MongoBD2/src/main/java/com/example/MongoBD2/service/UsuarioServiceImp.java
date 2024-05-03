package com.example.MongoBD2.service;

import com.example.MongoBD2.model.UsuarioModel;
import com.example.MongoBD2.repository.UsuarioRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
@Primary

public class UsuarioServiceImp implements UsuarioService{
    @Autowired
    UsuarioRepository usuarioRepository;

    @Override
    public String crearUsuario(UsuarioModel usuario){
        this.usuarioRepository.save(usuario);
        return "Tutor " + usuario.getNombre() + " creado";
    }

    @Override
    public List<UsuarioModel> listarUsuarios(){
        return this.usuarioRepository.findAll();
    }

    @Override
    public Optional<UsuarioModel> usuarioPorId(int usuarioid){
        return this.usuarioRepository.findById(usuarioid);
    }

    @Override
    public String actualizarUsuarioPorId(UsuarioModel usuario){
        this.usuarioRepository.save(usuario);
        return "Usuario " + usuario.getNombre() + " actualizado";
    }
}
