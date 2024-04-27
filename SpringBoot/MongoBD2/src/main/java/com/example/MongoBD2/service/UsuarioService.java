package com.example.MongoBD2.service;

import com.example.MongoBD2.model.UsuarioModel;
import java.util.List;
import java.util.Optional;

public interface UsuarioService {
    String crearUsuario(UsuarioModel usuario);
    List<UsuarioModel> listarUsuarios();
    Optional<UsuarioModel> usuarioPorId(int usuarioid);
    String eliminarUsuarioPorId(int usuarioid);
}
