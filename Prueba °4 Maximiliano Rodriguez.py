import os
os.system("cls")

"""Haga un programa que permita generar un menú de ingreso de usuarios. El menú principal
debe permitir mostrar 3 opciones:
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Al ingresar a la opción 1.-, se debe permitir ingresar nombre de usuario, sexo y contraseña
por separado. Para que el ingreso del usuario sea exitoso se debe cumplir lo siguiente: a) el
nombre de usuario no debe estar repetido, b) el sexo solo permite “F” o “M” y c) la contraseña
debe ser de largo mínimo 8 , debe tener al menos 1 número, debe tener al menos 1 letra y
no puede tener espacio en blanco. En caso de cumplir todas las condiciones, el usuario es
ingresado exitosamente.
Al ingresar la opción 2.-, el menú debe permitir buscar usuarios mediante el nombre de usua-
rio. Si el usuario existe, debe mostrar los datos asociados al usuario: sexo y contraseña. Si el
usuario no existe, debe mostrar un mensaje que el usuario no se encuentra.
Al ingresar la opción 3.-, el menú debe permitir eliminar al usuario y toda la información
asociada a este mediante el ingreso de un nombre de usuario por teclado. Si el usuario es
eliminado, se debe mostrar un mensaje como: “Usuario eliminado!”, pero en caso de que el
usuario no exista, se muestra un mensaje como: “No se pudo eliminar usuario!”.
Al ingresar la opción 4.-, el programa debe terminar.
Si se ingresa una opción distinta, debe mostrar un mensaje que debe seleccionar una opción
válida. Todas las opciones del menú deben estar implementas mediante funciones sepa-
radas del código principal (main)
Ejemplo:
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 1
Ingrese nombre de usuario: J.Rojas
Ingrese sexo: hombre
Debe ingresar M o F solamente. Intente de nuevo.
Ingrese sexo: M
Ingrese contraseña: 1234qwer
Contraseña valida.
Usuario ingresado con exito!!
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 1
Ingrese nombre de usuario: J.Rojas
Usuario ya existe. Intento otro.
Ingrese nombre de usuario: L.Pereira
Ingrese sexo: F
Ingrese contraseña: 12as34 df
Contraseña no valida. Intente otra.
Ingrese contraseña: as1234yuioj
Contraseña valida.
Usuario ingresado con exito!!
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 2
Ingrese usuario a buscar: L.Pereira
El sexo del usuario es: F y la contraseña es: as1234yuioj
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 2
Ingrese usuario a buscar: S.Castro
3
El usuario no se encuentra.
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 3
Ingrese usuario a buscar: L.Rojas
No se pudo eliminar usuario!
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 3
Ingrese usuario a buscar: L.Pereira
Usuario eliminado con éxito!
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 5
Debe ingresar una opción válida!!
MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.
Ingrese opción: 4
Programa terminado...
"""

usuarios = {}  
def validar_contrasena(contra):
    if len(contra) < 8:
        return False
    if not any(char.isdigit() for char in contra):
        return False
    if not any(char.isalpha() for char in contra):
        return False
    if ' ' in contra:
        return False
    return True
def ingresar_usuario():
    nom = input("Ingrese el nombre de usuario: ")
    if nom in usuarios:
        print("Usuario ya existe. Intente otro.")
        return

    sexo = input("Ingrese el sexo (F/M): ").upper()
    if sexo not in ['F', 'M']:
        print("Sexo inválido. Debe ser 'F' o 'M'.")
        return

    contra = input("Ingrese la contraseña (mínimo 8 caracteres, al menos 1 número y 1 letra, sin espacios): ")
    if not validar_contrasena(contra):
        contra = input("Contraseña inválida. Ingrese una nueva contraseña: ")
        if not validar_contrasena(contra):
            print("Contraseña inválida.")
            return
    usuarios[nom] = {'sexo': sexo, 'contrasena': contra}
    print("Usuario ingresado exitosamente.")

def buscar_usuario():
    nom = input("Ingrese el nombre de usuario a buscar: ")
    if nom in usuarios:
        print("Datos del usuario:")
        print("Sexo:", usuarios[nom]['sexo'])
        print("Contraseña:", usuarios[nom]['contrasena'])
    else:
        print("Usuario no encontrado.")

def eliminar_usuario():
    nom = input("Ingrese el nombre de usuario a eliminar: ")
    if nom in usuarios:
        del usuarios[nom]
        print("Usuario eliminado!")
    else:
        print("No se pudo eliminar usuario!")

def main():
    while True:
        print("\nMenú de opciones:")
        print("1.- Ingresar usuario.")
        print("2.- Buscar usuario.")
        print("3.- Eliminar usuario.")
        print("4.- Salir.")
        opci = input("Seleccione una opción: ")

        if opci == '1':
            ingresar_usuario()
        elif opci == '2':
            buscar_usuario()
        elif opci == '3':
            eliminar_usuario()
        elif opci == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
