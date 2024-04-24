import couchdb
import time
#conexión a la BD:

user = "JuanJaramillo"
pwd = "JuanEduardo12004"
host = "127.0.0.1"
port = "5984"

couch_server = couchdb.Server(f"http://{user}:{pwd}@{host}:{port}/")

db_name = "recommendation_system"

#selección o creación de un store existente:
if (db_name in couch_server):
    print("Conectado con la BD")
    db = couch_server[db_name]
else:
    print("Creando base de datos...")
    db = couch_server.create(db_name)

#Operaciones del crud:
#validacion al guardar documento
def validarGuardado(doc_id):
    try:
        doc = db[doc_id]
        print(f'El documento con id {doc_id} se ha guardado correctamente.')
    except couchdb.http.ResourceNotFound:
        print(f'Error al guardar. ')

#consultar documentos en DataBase
def consultar_documento(tipo,llave,valor):
    design_doc = f"_design/{tipo}"
    view_name = f"buscar_{llave}"
    
    # Verificar si el diseño y la vista existen
    try:
        db[design_doc]
    except couchdb.ResourceNotFound:
        print(f"La vista {design_doc} no existe")
        return ""

    # Utilizar la vista para buscar el documento por la llave
    try:        
        # Obtener el documento utilizando la vista
        resultados = db.view(f"{tipo}/{view_name}", key=valor)
        print("Dato encontrado")
        return [row.value for row in resultados]
    except couchdb.ResourceNotFound:
        print(f"No se encontro")
        time.sleep(1)
        return ""

#funciones de verificar existencia    
def verificar_curso(idCurso):
    # Buscar el curso por su ID
    cursos = consultar_documento("Curso", "id", idCurso)
    if cursos:
        return True
    else:
        return False

def verificar_aprendiz(idAprendiz):
    # Buscar el aprendiz por su ID
    aprendices = consultar_documento("Aprendiz", "id", idAprendiz)
    if aprendices:
        return True
    else:
        return False

def verificar_tutor(idTutor):
    # Buscar el tutor por su ID
    tutores = consultar_documento("Tutor", "id", idTutor)
    if tutores:
        return True
    else:
        return False
    
#funcion eliminacion de documento
def eliminacionDocumento(tipo,llave,valor):
    # Utilizar la vista correspondiente según el tipo de documento
    design_doc = f"_design/{tipo}"
    view_name = f"buscar_{llave}"

    # Verificar si el diseño y la vista existen
    try:
        db[design_doc]
    except couchdb.ResourceNotFound:
        print(f"El diseño '{design_doc}' y la vista '{view_name}' no existen.")
        time.sleep(1)
        return ""
    
    # Utilizar la vista para buscar el documento por la llave
    try:
        # Obtener el documento utilizando la vista
        resultados = db.view(f"{tipo}/{view_name}", key=valor)
        # Eliminamos los resultados encontrados uno por uno
        for row in resultados:
            db.delete(db[row.id])
        return print (f"{tipo} eliminado correctamente.")
    except couchdb.ResourceNotFound:
        print(f"No se encontraron documentos para la llave '{llave}' y el valor '{valor}'.")
        time.sleep(1)
        return ""

#funciones actualizar curso
def actualizar_curso_aprendiz(id, nombre, llave, valor):
    design_doc = f"_design/Curso"
    view_name = f"buscar_{llave}"
    
    try:
        db[design_doc]
    except couchdb.ResourceNotFound:
        print(f"El diseño {design_doc} no existe")
        return "Diseño no encontrado"

    try:
        resultados = db.view(f"Curso/{view_name}", key=valor)
        if len(resultados) == 0:
            print('No se encontraron los documentos que coincidan con la consulta')
            return 'No se encontraron los documentos que coincidan con la consulta'
        
        for row in resultados:
            # Obteniendo el documento
            doc_id = row.id
            doc = db[doc_id]
           
            # Actualizando el documento
            if 'aprendices' not in doc:
                doc['aprendices'] = []
            doc['aprendices'].append({"id":id, "nombre": nombre})
            
            # Guardando el documento actualizado
            db.save(doc)
        return "Documento actualizado correctamente."
    
    except couchdb.ResourceNotFound:
        print("No se encontró la vista.")
        time.sleep(1)
        return "Vista no encontrada"

def actualizar_curso_tutor(id, nombre, llave, valor):
    design_doc = f"_design/Curso"
    view_name = f"buscar_{llave}"
    
    try:
        db[design_doc]
    except couchdb.ResourceNotFound:
        print(f"El diseño {design_doc} no existe")
        return "Diseño no encontrado"

    try:
        resultados = db.view(f"Curso/{view_name}", key=valor)
        if len(resultados) == 0:
            print('No se encontraron los documentos que coincidan con la consulta')
            return 'No se encontraron los documentos que coincidan con la consulta'
        
        for row in resultados:
            # Obteniendo el documento
            doc_id = row.id
            doc = db[doc_id]
           
            if 'tutor' in doc:
                print('Ya hay un tutor asignado a este curso. No se puede agregar otro.')
                return 'Ya hay un tutor asignado a este curso. No se puede agregar otro.'
            
            # Actualizando el documento con el nuevo tutor
            doc['tutor'] = {"id": id, "nombre": nombre}
            
            # Guardando el documento actualizado
            db.save(doc)
        return "Documento actualizado correctamente"
    
    except couchdb.ResourceNotFound:
        print("No se encontró la vista.")
        time.sleep(1)
        return "Vista no encontrada"
    
#funcion busqueda de aprendices por curso
def busqueda_curso(tipo, llave, valor):
    design_doc = f"_design/{tipo}"
    view_name = f"buscar_{llave}"
    
    try:
        db[design_doc]
        
    except couchdb.ResourceNotFound:
        print(f"La vista {design_doc} no existe")
        return ""
    
    # Utilizar la vista para buscar el documento por la llave
    try:
        # Obtener el documento utilizando la vista
        resultados = db.view(f"{tipo}/{view_name}", key=valor)
        print("Dato encontrado")
        return [row.value for row in resultados]
    
    except couchdb.ResourceNotFound:
        print(f"No se encontro")
        time.sleep(1)
        return ""

# Menú de opciones 
def menu():
    while True:
        opcion = int(input('''---------------------------------------
Seleccione la opcion que desea
1. Creación
2. Consulta
3. Eliminar
4. Salir
Ingrese: '''))

        if opcion == 1:
            Opc_1 = int(input('''-----------------------------------
---¿Qué tipo de rol desea crear?---
1. Curso
2. Aprendiz
3. Tutor
Ingrese: '''))
            
            if Opc_1 == 1:
                while True:
                    id = input("Ingrese el ID del curso: ")
                    if verificar_curso(id):
                        print("Id Existente. Digite un Id diferente.")
                    else:
                        nombre = input("Ingrese el nombre del curso: ")
                        categoria = input("Ingrese la categoria del curso: ")
                        modalidad = input("Ingrese la modalidad del curso: ")
                        gratuito = True if input("¿El curso es gratuito? (V/F)\n Ingrese una opcion: ").upper() == "V" else False
                        precio = float(input("Ingrese el precio del curso: "))
                        duracion = int(input("Ingrese la duración del curso (horas): "))
                        certificado = True if input("¿El curso tiene certificado? (V/F)\n Ingrese una opcion: ").upper() ==  "V" else False
                        calPromedio = float(input("Ingrese la calificacion promedio del curso (0.0 a 5.0): "))
                        
                        curso = {
                            "tipo":"Curso",
                            "id":id,
                            "nombre":nombre,
                            "categoria":categoria,
                            "modalidad":modalidad,
                            "gratuito":gratuito,
                            "precio":precio,
                            "duracion":duracion,  
                            "certificado":certificado,
                            "calPromedio":calPromedio,
                            "aprendices": []
                        }
                        db.save(curso)
                        validarGuardado(curso["_id"])
                        break
                    pass
                        
            elif Opc_1 == 2:
                while True:
                    id = input("Ingrese el ID del aprendiz: ")
                    if verificar_aprendiz(id):
                        print("Id Existente. Digite un Id diferente.")
                    else:
                        nombre = input("Ingrese el nombre del aprendiz: ")
                        carrera = input("Ingrese la carrera del aprendiz: ")
                        semestre = int(input("Ingrese el semestre cursado del aprendiz: "))
                        idCursos = []
                        while True:
                            idCurso = str(input("Ingrese el ID del curso al que asiste el aprendiz (o 'fin' para terminar): "))
                            if idCurso.lower() == 'fin':
                                break
                            if verificar_curso(idCurso):
                                idCursos.append(idCurso)
                            else:
                                print(f"El ID digitado es erroneo. Por favor ingrese un ID válido: ")
                        aprendiz = {
                            "tipo":"Aprendiz",
                            "id":id,
                            "nombre":nombre,
                            "carrera":carrera,
                            "semestre":semestre,
                            "idCurso":idCursos
                        }
                        
                        db.save(aprendiz) 
                        for curso_id in idCursos:
                            actualizar_curso_aprendiz(id, nombre, "id", curso_id)
                            curso_aprendiz = {
                            "tipo" : "curso_aprendiz",
                            "idCurso" : idCursos,
                            "idAprendiz" : id
                        }
                        db.save(curso_aprendiz)                       
                        validarGuardado(aprendiz["_id"])
                        break
                    pass
            
            elif Opc_1 == 3:
                while True:
                    id = input("Ingrese el ID del tutor: ")
                    if verificar_tutor(id):
                        print("Id Existente. Digite un Id diferente.")
                    else:
                        nombre = input("Ingrese el nombre del tutor: ")
                        carrera = input("Ingrese la carrera del tutor: ")
                        semestre = int(input("Ingrese el semestre cursado del tutor: "))
                        calPromedio = float(input("Ingrese la calificacion promedio del tutor: "))
                                    
                        while True:
                            
                            idCurso = str(input("Ingrese el ID del curso que dicta el tutor: "))
                            if verificar_curso(idCurso):
                                curso = db.get(idCurso)
                                if curso and 'tutor' in curso:
                                    print("Ya hay un tutor asignado a este curso, por favor ingresa otro.")
                                else:
                                    print ("Tutor almacenado correctamente.")
                                    
                                    tutor = {
                                        "tipo":"Tutor",
                                        "id":id,
                                        "nombre":nombre,
                                        "carrera":carrera,
                                        "semestre":semestre,
                                        "calPromedio":calPromedio,
                                        "idCurso":idCurso
                                    }
                                    db.save(tutor)
                                    
                                    curso_tutor = {
                                        "tipo" : "curso_tutor",
                                        "idCurso" : idCurso,
                                        "idTutor" : id
                                    }
                                    db.save(curso_tutor)
                                    actualizar_curso_tutor(id, nombre, "id", idCurso)
                                    validarGuardado(tutor["_id"])
                                    break
                            else:
                                print("El ID digitado es erroneo. Por favor ingrese un ID valido.")
                                pass
                        break
            else:
                print("Opción Inválida. Proporcione una opción correcta.")    

        elif opcion == 2:
            Opc_2 = int(input('''---------------------------
---CONSULTA POR CRITERIO---
1. Consultar Curso
2. Consultar Aprendiz
3. Consultar Tutor
4. Consultar Aprendices por Curso
5. Regresar
Ingrese: '''))
            
            if Opc_2 == 1:
                tipo = "Curso"
                llave = str(input("Ingrese el criterio de búsqueda\nid, nombre, categoria, modalidad, gratuito, precio, duracion, certificado ó calPromedio: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                cursos = consultar_documento(tipo, llave, valor)
                print("Cursos encontrados:")
                for curso in cursos:
                    print(curso)
                    time.sleep(1)

            elif Opc_2 == 2:
                tipo = "Aprendiz"
                llave = str(input("Ingrese el criterio de búsqueda\nid, nombre, carrera ó semestre: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                aprendices = consultar_documento(tipo, llave, valor)
                print("Aprendices encontrados:")
                for aprendiz in aprendices:
                    print(aprendiz)
                    time.sleep(1)

            elif Opc_2 == 3:
                tipo = "Tutor"
                llave = str(input("Ingrese el criterio de búsqueda\nid, nombre, carrera ó semestre: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                tutores = consultar_documento(tipo, llave, valor)
                print("Tutores encontrados:")
                for tutor in tutores:
                    print(tutor)
                    time.sleep(1)
            
            elif Opc_2 == 4:
                tipo = "Curso"
                llave = "aprendices_curso"
                valor = input(f"Ingrese el id del curso que desea ver: ")
                curso_aprendiz = busqueda_curso(tipo, llave, valor)
                print(f"Aprendices del curso con id {valor} encontrados:")
                for curso_aprendiz in curso_aprendiz:
                    print(curso_aprendiz)
                    time.sleep(1)
                    
            elif Opc_2 == 5:
                continue  # Volver al menú principal
            else:
                print("Opción Inválida. Proporcione una opción correcta.")
        
        elif opcion ==3:
            Opc_3 = int(input('''---------------------------
---ELIMINACION---
1. Aprendiz
2. Tutor
3. Curso
4. Regresar
Ingrese: '''))
            
            if Opc_3 == 1:
                tipo = "Aprendiz"
                llave = str(input("Ingrese el criterio de eliminación\nid, nombre, carrera ó semestre: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                aprendices = eliminacionDocumento(tipo,llave,valor)
                time.sleep(1)
            
            elif Opc_3 == 2:
                tipo = "Tutor"
                llave = str(input("Ingrese el criterio de eliminación\nid, nombre, carrera, semestre ó calPromedio: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                tutores = eliminacionDocumento(tipo,llave,valor)
                time.sleep(1)
            
            elif Opc_3 == 3:
                tipo = "Curso"
                llave = str(input("Ingrese el criterio de eliminación\nid, nombre, categoria, modalidad, gratuito, precio, duracion, certificado ó calPromedio: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                cursos = eliminacionDocumento(tipo,llave,valor)
                time.sleep(1)
                    
            elif Opc_3 == 4:
                continue  # Volver al menú principal
            else:
                print("Opción Inválida. Proporcione una opción correcta.")
                    
            
        elif opcion == 4:
            print("Saliendo...")
            break  # Salir del bucle while y finalizar el programa
        
        else:
            print("Opción Inválida. Proporcione una opción correcta.")

menu()