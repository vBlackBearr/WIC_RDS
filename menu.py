from database import conexion, cursor


def cargar_contactos():
    # Lógica para cargar contactos desde la base de datos
    print("Método para cargar contactos. Implementa la lógica según tus necesidades.")


def crear_nuevo_contacto(current_user_id):
    print("Crear Nuevo Contacto:")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    calle = input("Calle: ")
    numero = input("Número: ")
    colonia = input("Colonia: ")
    cp = input("Código Postal: ")
    ciudad = input("Ciudad: ")

    try:
        # Insertar el nuevo contacto en la tabla 'persona'
        consulta_persona = "INSERT INTO persona (Nombre, Telefono, Correo, Calle, Numero, Colonia, CP, Ciudad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores_persona = (nombre, telefono, correo, calle, numero, colonia, cp, ciudad)

        cursor.execute(consulta_persona, valores_persona)
        conexion.commit()

        # Obtener el ID del nuevo contacto registrado
        id_nuevo_contacto = cursor.lastrowid

        print(f"Contacto '{nombre}' registrado con éxito. ID: {id_nuevo_contacto}")

        # Registrar el nuevo contacto en la tabla 'AgendaUsuario'
        consulta_agenda_usuario = "INSERT INTO AgendaUsuario (usuario_id, persona_id) VALUES (%s, %s)"
        valores_agenda_usuario = (current_user_id, id_nuevo_contacto)

        cursor.execute(consulta_agenda_usuario, valores_agenda_usuario)
        conexion.commit()

        print(f"Contacto '{nombre}' agregado a la agenda del usuario.")
    except Exception as e:
        print(f"Error al insertar el contacto: {e}")


def mostrar_agenda(current_user):
    print(f"Agenda de Contactos para el Usuario con ID {current_user}:\n")

    # Consulta para obtener los contactos del current_user
    consulta_agenda = """
        SELECT persona.id, persona.Nombre, persona.Telefono, persona.Correo
        FROM AgendaUsuario
        JOIN persona ON AgendaUsuario.persona_id = persona.id
        WHERE AgendaUsuario.usuario_id = %s
    """

    cursor.execute(consulta_agenda, (current_user,))
    contactos = cursor.fetchall()

    if contactos:
        # Imprimir encabezados
        print("{:<5} {:<20} {:<15} {:<30}".format("ID", "Nombre", "Teléfono", "Correo"))
        print("-" * 75)

        # Imprimir la información de cada contacto
        for contacto in contactos:
            id_contacto, nombre, telefono, correo = contacto
            print("{:<5} {:<20} {:<15} {:<30}".format(id_contacto, nombre, telefono, correo))
    else:
        print("La agenda está vacía.")


# def guardar_contacto():
#     print("Guardar Contacto:")
#     id_persona = input("Ingrese el ID del contacto a actualizar: ")
#
#     # Verificar si el ID de la persona existe en la tabla 'persona'
#     consulta_verificar_persona = "SELECT * FROM persona WHERE id = %s"
#     cursor.execute(consulta_verificar_persona, (id_persona,))
#     persona_existente = cursor.fetchone()
#
#     if persona_existente:
#         print("Datos actuales del contacto:")
#         print(persona_existente)
#
#         # Solicitar nueva información para actualizar el contacto
#         nuevo_nombre = input("Nuevo nombre (dejar en blanco para mantener el actual): ")
#         nuevo_telefono = input("Nuevo teléfono (dejar en blanco para mantener el actual): ")
#         nuevo_correo = input("Nuevo correo (dejar en blanco para mantener el actual): ")
#         nuevo_calle = input("Nueva calle (dejar en blanco para mantener la actual): ")
#         nuevo_numero = input("Nuevo número (dejar en blanco para mantener el actual): ")
#         nuevo_colonia = input("Nueva colonia (dejar en blanco para mantener la actual): ")
#         nuevo_cp = input("Nuevo código postal (dejar en blanco para mantener el actual): ")
#         nueva_ciudad = input("Nueva ciudad (dejar en blanco para mantener la actual): ")
#
#         # Construir la consulta de actualización
#         consulta_actualizar_persona = """
#             UPDATE persona
#             SET Nombre = COALESCE(%s, Nombre),
#                 Telefono = COALESCE(%s, Telefono),
#                 Correo = COALESCE(%s, Correo),
#                 Calle = COALESCE(%s, Calle),
#                 Numero = COALESCE(%s, Numero),
#                 Colonia = COALESCE(%s, Colonia),
#                 CP = COALESCE(%s, CP),
#                 Ciudad = COALESCE(%s, Ciudad)
#             WHERE id = %s
#         """
#
#         # Valores para la actualización
#         valores_actualizar_persona = (
#             nuevo_nombre, nuevo_telefono, nuevo_correo,
#             nuevo_calle, nuevo_numero, nuevo_colonia,
#             nuevo_cp, nueva_ciudad, id_persona
#         )
#
#         cursor.execute(consulta_actualizar_persona, valores_actualizar_persona)
#         conexion.commit()
#
#         print(f"Contacto con ID {id_persona} actualizado con éxito.")
#     else:
#         print(f"No se encontró un contacto con ID {id_persona}.")


def buscar_contacto_por_nombre(current_user):
    nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")

    # Consulta para buscar contactos por nombre
    consulta_buscar_nombre = """
        SELECT persona.id, persona.Nombre, persona.Telefono, persona.Correo
        FROM AgendaUsuario
        JOIN persona ON AgendaUsuario.persona_id = persona.id
        WHERE AgendaUsuario.usuario_id = %s AND persona.Nombre LIKE %s
    """

    cursor.execute(consulta_buscar_nombre, (current_user, f"%{nombre_buscar}%"))
    contactos_encontrados = cursor.fetchall()

    if contactos_encontrados:
        # Imprimir encabezados
        print("{:<5} {:<20} {:<15} {:<30}".format("ID", "Nombre", "Teléfono", "Correo"))
        print("-" * 75)

        # Imprimir la información de cada contacto encontrado
        for contacto in contactos_encontrados:
            id_contacto, nombre, telefono, correo = contacto
            print("{:<5} {:<20} {:<15} {:<30}".format(id_contacto, nombre, telefono, correo))
    else:
        print(f"No se encontraron contactos con el nombre '{nombre_buscar}'.")

# Ejemplo de uso
# buscar_contacto_por_nombre(current_user)



def buscar_contacto_por_telefono(current_user):
    telefono_buscar = input("Ingrese el número de teléfono del contacto a buscar: ")

    # Consulta para buscar contactos por número de teléfono
    consulta_buscar_telefono = """
        SELECT persona.id, persona.Nombre, persona.Telefono, persona.Correo
        FROM AgendaUsuario
        JOIN persona ON AgendaUsuario.persona_id = persona.id
        WHERE AgendaUsuario.usuario_id = %s AND persona.Telefono LIKE %s
    """

    cursor.execute(consulta_buscar_telefono, (current_user, f"%{telefono_buscar}%"))
    contactos_encontrados = cursor.fetchall()

    if contactos_encontrados:
        # Imprimir encabezados
        print("{:<5} {:<20} {:<15} {:<30}".format("ID", "Nombre", "Teléfono", "Correo"))
        print("-" * 75)

        # Imprimir la información de cada contacto encontrado
        for contacto in contactos_encontrados:
            id_contacto, nombre, telefono, correo = contacto
            print("{:<5} {:<20} {:<15} {:<30}".format(id_contacto, nombre, telefono, correo))
    else:
        print(f"No se encontraron contactos con el número de teléfono '{telefono_buscar}'.")



def borrar_contacto():
    print("Borrar Contacto:")
    id_contacto_borrar = input("Ingresa el ID del contacto a borrar: ")
    # Lógica para borrar un contacto de la base de datos
    print(f"Método para borrar el contacto con ID: {id_contacto_borrar}. Implementa la lógica según tus necesidades.")
