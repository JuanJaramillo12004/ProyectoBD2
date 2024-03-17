import couchdb
import time
#conexión a la BD:

user = "JuanJaramillo"
pwd = "JuanEduardo12004"
host = "127.0.0.1"
port = "5984"

#couch_server  = couchdb.Server("http://admin:admin@127.0.0.1:5984/")
couch_server = couchdb.Server(f"http://{user}:{pwd}@{host}:{port}/")

db_name = "recommendation_system"

#selección o creación de un store existente:
if (db_name in couch_server):
    print("Conectado con la BD")
    db = couch_server[db_name]
else:
    print("---Creando base de datos")
    db = couch_server.create(db_name)

#Operaciones del crud:
def validarGuardado(doc_id):
    try:
        doc = db[doc_id]
        print(f'El documento con id {doc_id} se ha guardado correctamente.')
    except couchdb.http.ResourceNotFound:
        print(f'Error al guardar. ')
        
def consultar_documento(tipo,llave,valor):
    design_doc = f"_design/{tipo}"
    view_name = f"buscar_{llave}"
    
    try:
        db[design_doc]
    except couchdb.ResourceNotFound:
        print(f"La vista {design_doc} no existe")
        return ""
    
    try:
        resultados = db.view(f"{tipo}/{view_name}", key=valor)
        print("Dato encontrado")
        return [row.value for row in resultados]
    except couchdb.ResourceNotFound:
        print(f"No se encontro")
        time.sleep(1)
        return ""
#funcion eliminacion de documento
def eliminacionDocumentoId(tipo,llave,valor):
    # Utilizar la vista correspondiente según el tipo de documento
    design_doc = f"_design/{tipo}"
    view_name = f"buscar_por_{llave}"

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
        return "Documentos eliminados correctamente."
    except couchdb.ResourceNotFound:
        print(f"No se encontraron documentos para la llave '{llave}' y el valor '{valor}'.")
        time.sleep(1)
        return ""

#cambios al menu 
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
1. Aprendiz
2. Tutor
3. Curso
Ingrese: '''))
            
            if Opc_1 == 1:
                id = input("Ingrese el ID del aprendiz: ")
                nombre = input("Ingrese el nombre del aprendiz: ")
                carrera = input("Ingrese la carrera del aprendiz: ")
                semestre = int(input("Ingrese el semestre cursado del aprendiz: "))
                aprendiz = {
                    "tipo":"Aprendiz",
                    "id":id,
                    "nombre":nombre,
                    "carrera":carrera,
                    "semestre":semestre
                }
                db.save(aprendiz)
                validarGuardado(aprendiz["_id"])
                pass
            
            elif Opc_1 == 2:
                id = input("Ingrese el ID del tutor: ")
                nombre = input("Ingrese el nombre del tutor: ")
                carrera = input("Ingrese la carrera del tutor: ")
                semestre = int(input("Ingrese el semestre cursado del tutor: "))
                calPromedio = float(input("Ingrese la calificacion promedio del tutor: "))

                tutor = {
                    "tipo":"Tutor",
                    "id":id,
                    "nombre":nombre,
                    "carrera":carrera,
                    "semestre":semestre,
                    "calPromedio":calPromedio
                }
                db.save(tutor)
                validarGuardado(tutor["_id"])
                pass
                

            elif Opc_1 == 3:
                id = input("Ingrese el ID del curso: ")
                nombre = input("Ingrese el nombre del curso: ")
                categoria = input("Ingrese la categoria del curso: ")
                modalidad = input("Ingrese la modalidad del curso: ")
                gratuito = True if input("¿El curso es gratuito? (V/F)\n Ingrese una opcion: ").upper() == "V" else False
                precio = float(input("Ingrese el precio del curso: "))
                duracion = int(input("Ingrese la duración del curso: "))
                certificado = True if input("¿El curso tiene certificado? (V/F)\n Ingrese una opcion: ").upper() ==  "V" else False
                calPromedio = float(input("Ingrese la calificacion promedio del curso: "))
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
                    "calPromedio":calPromedio
                }
                db.save(curso)
                validarGuardado(curso["_id"])
                pass
            else:
                print("Opción Inválida. Proporcione una opción correcta.")
        
        elif opcion == 2:
            Opc_2 = int(input('''---------------------------
---CONSULTA POR CRITERIO---
1. Consultar Aprendiz
2. Consultar Tutor
3. Consultar Curso
4. Regresar
Ingrese: '''))
            
            if Opc_2 == 1:
                tipo = "Aprendiz"
                llave = str(input("Ingrese el criterio de búsqueda:\nid, nombre, carrera ó semestre: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                aprendices = consultar_documento(tipo, llave, valor)
                print("Aprendices encontrados:")
                for aprendiz in aprendices:
                    print(aprendiz)
                    time.sleep(1)

            elif Opc_2 == 2:
                tipo = "Tutor"
                llave = str(input("Ingrese el criterio de búsqueda:\nid, nombre, carrera, semestre ó calPromedio: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                tutores = consultar_documento(tipo, llave, valor)
                print("Tutores encontrados:")
                for tutor in tutores:
                    print(tutor)
                    time.sleep(1)
                    
            elif Opc_2 == 3:
                tipo = "Curso"
                llave = str(input("Ingrese el criterio de búsqueda:\nid, nombre, categoria, modalidad, gratuito, precio, duracion, certificado ó calPromedio: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                cursos = consultar_documento(tipo, llave, valor)
                print("Cursos encontrados:")
                for curso in cursos:
                    print(curso)
                    time.sleep(1)
                    
            elif Opc_2 == 4:
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
                llave = str(input("Ingrese el criterio de búsqueda:\nid, nombre, carrera ó semestre: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                aprendices = eliminacionDocumentoId(tipo,llave,valor)
                print("Aprendices eliminados:")
                for aprendiz in aprendices:
                    print(aprendiz)
                    time.sleep(1)
            
            elif Opc_3 == 2:
                tipo = "Tutor"
                llave = str(input("Ingrese el criterio de búsqueda:\nid, nombre, carrera, semestre ó calPromedio: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                tutores = eliminacionDocumentoId(tipo,llave,valor)
                print("Tutores eliminados:")
                for tutor in tutores:
                    print(tutor)
                    time.sleep(1)
            
            elif Opc_3 == 3:
                tipo = "Curso"
                llave = str(input("Ingrese el criterio de búsqueda:\nid, nombre, categoria, modalidad, gratuito, precio, duracion, certificado ó calPromedio: ")).lower()
                valor = input(f"Ingrese el valor del criterio '{llave}': ")
                cursos = eliminacionDocumentoId(tipo,llave,valor)
                print("Cursos eliminados:")
                for curso in cursos:
                    print(curso)
                    time.sleep(1)
                    
            elif Opc_3 == 4:
                continue  # Volver al menú principal
            else:
                print("Opción Inválida. Proporcione una opción correcta.")
                    
            
        elif opcion == 4:
            print("Salir")
            break  # Salir del bucle while y finalizar el programa
        
        else:
            print("Opción Inválida. Proporcione una opción correcta.")

menu()
