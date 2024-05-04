package com.example.MongoBD2.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "Calificaciones")
@Data
@AllArgsConstructor
@NoArgsConstructor

public class CalificacionModel {
    @Id
    private Integer _id;
    private Integer cursoid;
    private Double calificacion;
}
