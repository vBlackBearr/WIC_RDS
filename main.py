from database import cursor, conexion
from menu import crear_nuevo_contacto, mostrar_agenda, buscar_contacto_por_nombre, buscar_contacto_por_telefono


def menu(current_user):
    while True:
        print("1) Cargar contactos")
        print("2) Crear nuevo contacto")
        print("3) Mostrar agenda")
        print("4) Buscar Contacto por nombre")
        print("5) Buscar Contacto por telefono")
        print("6) Borrar contacto")
        print("0) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("")

        elif opcion == "2":
            crear_nuevo_contacto(current_user)
        elif opcion == "3":
            mostrar_agenda(current_user)
        elif opcion == "4":
            buscar_contacto_por_nombre(current_user)
        elif opcion == "5":
            buscar_contacto_por_telefono(current_user)
        elif opcion == "6":
            # Lógica para la opción 6
            print("Seleccionaste la opción 6: Borrar contacto")
        elif opcion == "0":
            # Salir del bucle si el usuario selecciona la opción 0
            print("Saliendo del programa. Hasta luego!")
            break
        else:
            # Mensaje de error para opciones no válidas
            print("Opción no válida. Por favor, selecciona una opción válida.")



def registrar_usuario():
    print("Registro de Usuario:")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    calle = input("Calle: ")
    numero = input("Número: ")
    colonia = input("Colonia: ")
    cp = input("Código Postal: ")
    ciudad = input("Ciudad: ")

    # Insertar el nuevo usuario en la tabla 'persona'
    consulta_persona = "INSERT INTO persona (Nombre, Telefono, Correo, Calle, Numero, Colonia, CP, Ciudad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores_persona = (nombre, telefono, correo, calle, numero, colonia, cp, ciudad)

    cursor.execute(consulta_persona, valores_persona)
    conexion.commit()

    # Obtener el ID del nuevo usuario registrado
    id_nuevo_usuario = cursor.lastrowid

    # Solicitar y almacenar la contraseña
    contraseña = input("Contraseña: ")

    # Insertar el nuevo usuario en la tabla 'usuarios'
    consulta_usuarios = "INSERT INTO usuarios (id_persona, Contraseña, PermisoAgenda) VALUES (%s, %s, %s)"
    valores_usuarios = (id_nuevo_usuario, contraseña, True)

    cursor.execute(consulta_usuarios, valores_usuarios)
    conexion.commit()

    print("Usuario registrado con éxito!")


def iniciar_sesion():
    print("Inicio de Sesión:")
    email_login = input("Correo: ")
    pass_login = input("Contraseña: ")

    # Verificar las credenciales en la base de datos
    consulta = "SELECT usuarios.id FROM usuarios JOIN persona ON usuarios.id_persona = persona.id WHERE Correo = %s AND Contraseña = %s"
    valores = (email_login, pass_login)

    cursor.execute(consulta, valores)
    resultado = cursor.fetchone()

    if resultado:
        id_usuario = resultado[0]
        print(f"¡Inicio de sesión exitoso! ID de usuario: {id_usuario}")
        return id_usuario
    else:
        print("Credenciales incorrectas. Inténtalo nuevamente.")
        # Llamada recursiva en caso de fallo
        return iniciar_sesion()


def main():
    while True:
        print("Bienvenido a Agenda!!")
        print("")
        print("1) Iniciar Sesion")
        print("2) Registrarse")

        op_session = input()

        current_user = 0
        if op_session == "1":
            # current_user = iniciar_sesion()
            current_user = 1
            break
        elif op_session == "2":
            registrar_usuario()
        else:
            print("Opción no válida. Inténtalo nuevamente.")

    menu(current_user)


if __name__ == "__main__":
    main()
