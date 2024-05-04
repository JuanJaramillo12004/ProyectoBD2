package com.example.MongoBD2.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "Tutores")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class TutorModel {
    @Id
    private Integer _id;
    private String nombre;
    private String facultad;
}
