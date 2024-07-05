import numpy as np

def is_number():
    while True:
        try:
            x = input("Ingrese un número: ")
            x = int(x)
            return x
        except ValueError:
            print("Error, debe ingresar un número, reintente nuevamente.")

def is_medication():
    while True:
        try:
            x = input("Ingrese un medicamento: ")
            x = str(x)
            return x
        except ValueError:
            print("Error, reintente nuevamente.")

def show_menu():
    print("\nSERVICIO DE ATENCIÓN MÉDICA DE URGENCIAS")
    print("--------------------------------------------")
    print("1) Ingresar Ficha del Paciente")
    print("2) Buscar Ficha por Rut")
    print("3) Buscar Medicamentos por Rut")
    print("4) Eliminar Ficha del Paciente")
    print("5) Listar Pacientes Atendidos")
    print("6) Salir")
    print("--------------------------------------------")

def is_valid_rut():
    while True:
        x = input("Ingrese un RUT válido: ")
        if x == "":
            print("Error, debe ingresar un RUT válido, reintente nuevamente.")
        else:
            return x

pacientes = np.empty([50, 7], dtype="object")
index = 0

while True:
    show_menu()
    option = is_number()

    if option == 1:
        for i in range(0, 7):
            if i == 0:
                pacientes[index, i] = input("Ingrese el nombre del paciente: ")
            elif i == 1:
                pacientes[index, i] = is_valid_rut()
            elif i == 2:
                pacientes[index, i] = is_number()
            elif i == 3:
                pacientes[index, i] = input("Ingrese el sexo del paciente: ")
            elif i == 4:
                pacientes[index, i] = input("Ingrese la dirección del paciente: ")
            elif i == 5:
                pacientes[index, i] = input("Ingrese el diagnóstico del paciente: ")
            elif i == 6:
                pacientes[index, i] = is_medication()

        index += 1
        print("Ficha del paciente ingresada correctamente.")
        print("--------------------------------------------")

    elif option == 2:
        rut_busqueda = is_valid_rut()

        for i in range(index):
            if pacientes[i, 1] == rut_busqueda:
                print(f"Nombre: {pacientes[i, 0]}")
                print(f"RUT: {pacientes[i, 1]}")
                print(f"Edad: {pacientes[i, 2]}")
                print(f"Sexo: {pacientes[i, 3]}")
                print(f"Dirección: {pacientes[i, 4]}")
                print(f"Diagnóstico: {pacientes[i, 5]}")
                print(f"Medicamento: {pacientes[i, 6]}")
                print("--------------------------------------------")
                break
        else:
            print("Error, RUT no encontrado.")
            print("--------------------------------------------")

    elif option == 3:
        rut_busqueda = is_valid_rut()

        for i in range(index):
            if pacientes[i, 1] == rut_busqueda:
                print(f"Medicamento: {pacientes[i, 6]}")
                print("--------------------------------------------")
                break
        else:
            print("Error, RUT no encontrado.")
            print("--------------------------------------------")

    elif option == 4:
        rut_busqueda = is_valid_rut()

        for i in range(index):
            if pacientes[i, 1] == rut_busqueda:
                pacientes = np.delete(pacientes, i, axis=0)
                index -= 1
                print("Ficha del paciente eliminada correctamente.")
                print("--------------------------------------------")
                break
        else:
            print("Error, RUT no encontrado.")
            print("--------------------------------------------")

    elif option == 5:
        print("Listado de pacientes atendidos:")
        for i in range(index):
            if pacientes[i, 0] != "":
                print(f"Nombre: {pacientes[i, 0]}")
                print(f"RUT: {pacientes[i, 1]}")
                print(f"Edad: {pacientes[i, 2]}")
                print(f"Sexo: {pacientes[i, 3]}")
                print(f"Dirección: {pacientes[i, 4]}")
                print(f"Diagnóstico: {pacientes[i, 5]}")
                print(f"Medicamento: {pacientes[i, 6]}")
                print("--------------------------------------------")

    elif option == 6:
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida, reintente nuevamente.")
