

# Agregar algoritmo para validacion de usuario
def Login():
    print("Bienvenido a Agenda!!")
    print("")
    print("1) Iniciar Sesion")
    print("2) Registrarse")

    op_session = input()

    if op_session == 1:
        while True:
            email_login = input("\nIngresa email:")
            pass_login = input("\nIngresa contraseña")



    elif op_session == 2:
        while True:
            email_login = input("\nIngresa email:")
            pass_login = input("\nIngresa contraseña")


def Menu():
    print("1) Cargar contactos")
    print("2) Crear nuevo contacto")
    print("3) Guardar contacto")
    print("4) Buscar Contacto por nombre")
    print("5) Buscar Contacto por telefono")
    print("6) Borrar contacto")

def main():
    Login()
    Menu()



