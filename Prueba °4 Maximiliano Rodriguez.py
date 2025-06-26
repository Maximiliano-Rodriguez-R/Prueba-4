import os
os.system("cls")


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
