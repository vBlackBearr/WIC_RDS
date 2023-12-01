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


def borrar_contacto(current_user):
    # Mostrar la lista de contactos disponibles para borrar
    mostrar_agenda(current_user)

    try:
        # Solicitar al usuario que elija el contacto a borrar
        id_contacto_borrar = int(input("Ingrese el ID del contacto que desea borrar (0 para cancelar): "))

        if id_contacto_borrar == 0:
            print("Operación de borrado cancelada.")
            return

        # Consulta para obtener información del contacto seleccionado
        consulta_contacto = """
            SELECT persona.Nombre, persona.Telefono, persona.Correo
            FROM AgendaUsuario
            JOIN persona ON AgendaUsuario.persona_id = persona.id
            WHERE AgendaUsuario.usuario_id = %s AND persona.id = %s
        """

        cursor.execute(consulta_contacto, (current_user, id_contacto_borrar))
        contacto_seleccionado = cursor.fetchone()

        if not contacto_seleccionado:
            print(f"No se encontró un contacto con el ID {id_contacto_borrar}.")
            return

        nombre, telefono, correo = contacto_seleccionado

        # Confirmar la eliminación
        confirmacion = input(
            f"¿Está seguro de que desea borrar a '{nombre}' con teléfono '{telefono}' y correo '{correo}'? (S/N): ")

        if confirmacion.upper() == "S":
            # Eliminar el contacto de la tabla 'AgendaUsuario'
            consulta_eliminar = "DELETE FROM AgendaUsuario WHERE usuario_id = %s AND persona_id = %s"
            cursor.execute(consulta_eliminar, (current_user, id_contacto_borrar))
            conexion.commit()

            print(f"Contacto '{nombre}' borrado exitosamente.")
        else:
            print("Operación de borrado cancelada.")
    except ValueError:
        print("Por favor, ingrese un ID válido.")


def permisos_agenda_personal(current_user):
    # Obtener el valor actual de PermisoAgenda
    consulta_permisos = "SELECT PermisoAgenda FROM usuarios WHERE id = %s"
    cursor.execute(consulta_permisos, (current_user,))
    permiso_actual = cursor.fetchone()

    if not permiso_actual:
        print("No se encontró información de permisos para el usuario.")
        return

    permiso_actual = permiso_actual[0]

    # Mostrar el estado actual de los permisos
    estado_actual = "Pública" if permiso_actual else "Privada"
    print(f"El estado actual de la agenda es: {estado_actual}")

    # Solicitar al usuario que cambie el estado si lo desea
    cambio_permisos = input("¿Desea cambiar el estado de la agenda? (S/N): ")

    if cambio_permisos.upper() == "S":
        # Cambiar el valor de PermisoAgenda
        nuevo_estado = not permiso_actual  # Cambiar entre True (Pública) y False (Privada)
        consulta_cambio_permisos = "UPDATE usuarios SET PermisoAgenda = %s WHERE id = %s"
        cursor.execute(consulta_cambio_permisos, (nuevo_estado, current_user))
        conexion.commit()

        print(f"Estado de la agenda actualizado a {'Pública' if nuevo_estado else 'Privada'}.")
    else:
        print("Operación cancelada. El estado de la agenda no ha cambiado.")


def invitar_a_mi_agenda(current_user):
    # Mostrar la lista de usuarios disponibles para invitar
    consulta_usuarios = "SELECT id, id_persona FROM usuarios WHERE id != %s"
    cursor.execute(consulta_usuarios, (current_user,))
    usuarios_disponibles = cursor.fetchall()

    if not usuarios_disponibles:
        print("No hay otros usuarios disponibles para invitar.")
        return

    print("Lista de Usuarios Disponibles para Invitar:")
    print("{:<5} {:<15}".format("ID", "Nombre"))
    print("-" * 25)

    for usuario in usuarios_disponibles:
        id_usuario, id_persona = usuario
        # Obtener el nombre de la persona correspondiente al usuario
        consulta_nombre_persona = "SELECT Nombre FROM persona WHERE id = %s"
        cursor.execute(consulta_nombre_persona, (id_persona,))
        nombre_persona = cursor.fetchone()[0]

        print("{:<5} {:<15}".format(id_usuario, nombre_persona))

    try:
        # Solicitar al usuario que elija a quién invitar
        id_usuario_invitar = int(input("Ingrese el ID del usuario al que desea invitar (0 para cancelar): "))

        if id_usuario_invitar == 0:
            print("Operación de invitación cancelada.")
            return

        # Mostrar opciones de tipo de permiso
        print("Opciones de Tipo de Permiso:")
        consulta_tipos_permiso = "SELECT id, permiso FROM TipoPermiso"
        cursor.execute(consulta_tipos_permiso)
        tipos_permiso = cursor.fetchall()

        for tipo_permiso in tipos_permiso:
            id_tipo_permiso, permiso = tipo_permiso
            print(f"{id_tipo_permiso}: {permiso}")

        # Solicitar al usuario que elija el tipo de permiso
        id_tipo_permiso = int(input(
            "Ingrese el ID del tipo de permiso (1 para solo lectura, 2 para lectura y escritura, 3 para bloqueado): "))

        id_tipo_invitacion = 1

        # Crear la invitación en la base de datos
        consulta_invitar = """
            INSERT INTO Invitaciones (grantor, grantee, tipo_permiso_a_dar, tipo_invitacion_id, estado_invitacion_id)
            VALUES (%s, %s, %s, %s, 1)
        """
        cursor.execute(consulta_invitar, (current_user, id_usuario_invitar, id_tipo_permiso, id_tipo_invitacion))
        conexion.commit()

        print("Invitación enviada correctamente.")
    except ValueError:
        print("Por favor, ingrese un ID válido.")


def ver_invitaciones(current_user):
    # Obtener las invitaciones pendientes para el usuario actual
    consulta_invitaciones = """
        SELECT i.grantor, p.Nombre, i.tipo_invitacion_id, i.tipo_permiso_a_dar
        FROM Invitaciones i
        JOIN persona p ON i.grantor = p.id
        WHERE i.grantee = %s AND i.estado_invitacion_id = 1
    """
    cursor.execute(consulta_invitaciones, (current_user,))
    invitaciones = cursor.fetchall()

    if not invitaciones:
        print("No tienes invitaciones pendientes.")
        return

    print("Invitaciones Pendientes:")
    print("{:<5} {:<15} {:<30} {:<20}".format("ID", "Nombre", "Tipo de Invitación", "Permiso"))
    print("-" * 80)

    for invitacion in invitaciones:
        grantor, nombre_grantor, tipo_invitacion_id, tipo_permiso_a_dar = invitacion

        # Obtener el texto del tipo de invitación
        texto_tipo_invitacion = ""
        if tipo_invitacion_id == 1:
            texto_tipo_invitacion = "te ha invitado a ver su agenda"
        elif tipo_invitacion_id == 2:
            texto_tipo_invitacion = "te ha solicitado que le brindes acceso a tu agenda"
        elif tipo_invitacion_id == 3:
            texto_tipo_invitacion = "te ha invitado a mezclar sus agendas"

        # Obtener el texto del tipo de permiso (si no es una invitación de tipo 3)
        texto_permiso = ""
        if tipo_invitacion_id != 3:
            consulta_tipo_permiso = "SELECT permiso FROM TipoPermiso WHERE id = %s"
            cursor.execute(consulta_tipo_permiso, (tipo_permiso_a_dar,))
            tipo_permiso = cursor.fetchone()[0]
            texto_permiso = f"permiso: {tipo_permiso}"

        print("{:<5} {:<15} {:<30} {:<20}".format(grantor, nombre_grantor, texto_tipo_invitacion, texto_permiso))

    try:
        # Solicitar al usuario que elija una invitación para responder
        id_invitacion_responder = int(
            input("Ingrese el ID de la invitación a la que desea responder (0 para cancelar): "))

        if id_invitacion_responder == 0:
            print("Operación de respuesta a invitación cancelada.")
            return

        # Solicitar al usuario que elija aceptar o rechazar la invitación
        respuesta_invitacion = input("¿Desea aceptar (A) o rechazar (R) la invitación?: ").upper()

        if respuesta_invitacion == "A":
            # Aceptar la invitación
            consulta_aceptar_invitacion = "UPDATE Invitaciones SET estado_invitacion_id = 2 WHERE grantor = %s AND grantee = %s"
            cursor.execute(consulta_aceptar_invitacion, (grantor, current_user))

            # aceptar_invitacion(current_user, )
            

            conexion.commit()
            print("Invitación aceptada.")
        elif respuesta_invitacion == "R":
            # Rechazar la invitación
            consulta_rechazar_invitacion = "UPDATE Invitaciones SET estado_invitacion_id = 2 WHERE grantor = %s AND grantee = %s"
            cursor.execute(consulta_rechazar_invitacion, (grantor, current_user))
            conexion.commit()
            print("Invitación rechazada.")
        else:
            print("Respuesta no válida. Operación cancelada.")
    except ValueError:
        print("Por favor, ingrese un ID válido.")


def grant_permisos(grantor, grantee, tipo_permiso_a_dar):
    # Insertar el nuevo registro en la tabla PermisosPersonales
    consulta_insertar_permiso = """
        INSERT INTO PermisosPersonales (grantor, grantee, tipo_permiso_id)
        VALUES (%s, %s, %s)
    """
    cursor.execute(consulta_insertar_permiso, (grantor, grantee, tipo_permiso_a_dar))
    conexion.commit()
    print("Permisos personales creados correctamente.")


def aceptar_invitacion(current_user, grantor, grantee, tipo_permiso_a_dar, tipo_invitacion_id):
    # Actualizar el estado de la invitación a "concluida"
    consulta_aceptar_invitacion = "UPDATE Invitaciones SET estado_invitacion_id = 2 WHERE grantor = %s AND grantee = %s"
    cursor.execute(consulta_aceptar_invitacion, (grantor, grantee))
    conexion.commit()
    print("Invitación aceptada.")

    # Determinar el grantor y el grantee según el tipo de invitación
    if tipo_invitacion_id == 1:
        grantor_id = grantor
        grantee_id = grantee
    elif tipo_invitacion_id == 2:
        grantor_id = current_user
        grantee_id = grantor
    else:
        # Manejar otros tipos de invitaciones según sea necesario
        grantor_id = current_user
        grantee_id = grantor

    # Llamar al método para conceder permisos
    grant_permisos(grantor_id, grantee_id, tipo_permiso_a_dar)
    print("Permisos otorgados")
