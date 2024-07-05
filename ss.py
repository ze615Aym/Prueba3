import numpy as np
import json
import os

def is_num():
    while True:
        try:
            x = input("Ingrese una opción: ")
            x = int(x)
            return x
        except ValueError:
            print("Error, debe ingresar un número, reintente.")

def is_medicamento():
    while True:
        try:
            x = input("Ingrese un medicamento: ")
            x = str(x)
            return x
        except ValueError:
            print("Error, debe ingresar un número, reintente.")

def is_valid_rut():
    while True:
        try:
            x = input("Ingrese un rut: ")
            x = str(x)
            return x
        except ValueError:
            print("Error, debe ingresar un número, reintente.")

def show_menu():
    print("\nSERVICIO DE ATENCIÓN MÉDICA DE URGENCIAS")
    print("--------------------------------------------")
    print("1) Ingresar Ficha del Paciente")
    print("2) Buscar Ficha por Rut")
    print("3) Buscar Medicamentos por Rut")
    print("4) Eliminar Ficha del Paciente")
    print("5) Listar Pacientes Atendidos")
    print("6) Listar Pacientes Ingresados")
    print("7) Salir")
    print("--------------------------------------------")

def mostrar_posiciones_pacientes(pacientes, num_pacientes):
    print("\nPosiciones ocupadas en la lista de pacientes:")
    for i in range(num_pacientes):
        if pacientes[i, 0] != "":
            print(f"Posición {i}: {pacientes[i, 0]}")
    print("--------------------------------------------")

# Iniciar la matriz
pacientes = np.empty([50, 7], dtype="object")
num_pacientes = 0

# Leer datos de los archivos JSON y TXT
if os.path.exists("pacientes.json"):
    with open("pacientes.json", "r") as archivo_json:
        data = json.load(archivo_json)
        for paciente in data["pacientes"]:
            encontrado = False
            for i in range(num_pacientes):
                if pacientes[i, 1] == paciente["rut"]:
                    encontrado = True
                    break
            if not encontrado:
                pacientes[num_pacientes] = [
                    paciente["nombre"],
                    paciente["rut"],
                    paciente["edad"],
                    paciente["sexo"],
                    paciente["direccion"],
                    paciente["diagnostico"],
                    paciente["medicamento"]
                ]
                num_pacientes += 1

if os.path.exists("pacientes.txt"):
    with open("pacientes.txt", "r") as archivo_txt:
        for linea in archivo_txt:
            if linea.startswith("Nombre:"):
                nombre = linea.split(":")[1].strip()
                rut = archivo_txt.readline().split(":")[1].strip()
                edad = archivo_txt.readline().split(":")[1].strip()
                sexo = archivo_txt.readline().split(":")[1].strip()
                direccion = archivo_txt.readline().split(":")[1].strip()
                diagnostico = archivo_txt.readline().split(":")[1].strip()
                medicamento = archivo_txt.readline().split(":")[1].strip()
                encontrado = False
                for i in range(num_pacientes):
                    if pacientes[i, 1] == rut:
                        encontrado = True
                        break
                if not encontrado:
                    pacientes[num_pacientes] = [nombre, rut, edad, sexo, direccion, diagnostico, medicamento]
                    num_pacientes += 1
                archivo_txt.readline() 
                
while True:
    show_menu()
    opcion = is_num()

    if opcion == 1:
        paciente = [
            input("Ingrese el nombre del paciente: "),
            is_valid_rut(),
            input("Ingrese la edad del paciente: "),
            input("Ingrese el sexo del paciente: "),
            input("Ingrese la dirección del paciente: "),
            input("Ingrese el diagnóstico del paciente: "),
            is_medicamento()
        ]

        # Verificar si ya existe un paciente con el mismo RUT
        duplicado_encontrado = False
        for i in range(num_pacientes):
            if pacientes[i, 1] == paciente[1]:
                print("Error: El RUT ya existe, ingrese un RUT diferente.")
                duplicado_encontrado = True
                break

        if not duplicado_encontrado:
            pacientes[num_pacientes] = paciente
            num_pacientes += 1
            print("Ficha del paciente ingresada correctamente.")
            print("--------------------------------------------")
            mostrar_posiciones_pacientes(pacientes, num_pacientes)

    elif opcion == 2:
        rut_busqueda = is_valid_rut()
        encontrado = False
        for i in range(num_pacientes):
            if pacientes[i, 1] == rut_busqueda:
                print(f"Nombre: {pacientes[i, 0]}")
                print(f"RUT: {pacientes[i, 1]}")
                print(f"Edad: {pacientes[i, 2]}")
                print(f"Sexo: {pacientes[i, 3]}")
                print(f"Dirección: {pacientes[i, 4]}")
                print(f"Diagnóstico: {pacientes[i, 5]}")
                print(f"Medicamento: {pacientes[i, 6]}")
                print("--------------------------------------------")
                encontrado = True
                break
        if not encontrado:
            print("Error, RUT no encontrado.")
            print("--------------------------------------------")
    elif opcion == 3:
        rut_busqueda = is_valid_rut()
        encontrado = False
        for i in range(num_pacientes):
            if pacientes[i, 1] == rut_busqueda:
                print(f"Medicamento: {pacientes[i, 6]}")
                print("--------------------------------------------")
                encontrado = True
                break
        if not encontrado:
            print("Error, RUT no encontrado.")
            print("--------------------------------------------")
    elif opcion == 4:
        rut_busqueda = is_valid_rut()
        encontrado = False
        for i in range(num_pacientes):
            if pacientes[i, 1] == rut_busqueda:
                pacientes[i] = ["", "", "", "", "", "", ""]
                num_pacientes -= 1
                print("Ficha del paciente eliminada correctamente.")
                print("--------------------------------------------")
                mostrar_posiciones_pacientes(pacientes, num_pacientes)
                encontrado = True
                break
        if not encontrado:
            print("Error, RUT no encontrado.")
            print("--------------------------------------------")
    elif opcion == 5:
        print("Listado de pacientes atendidos:")
        for i in range(num_pacientes):
            if pacientes[i, 0] != "":
                print(f"Nombre: {pacientes[i, 0]}")
                print(f"RUT: {pacientes[i, 1]}")
                print(f"Edad: {pacientes[i, 2]}")
                print(f"Sexo: {pacientes[i, 3]}")
                print(f"Dirección: {pacientes[i, 4]}")
                print(f"Diagnóstico: {pacientes[i, 5]}")
                print(f"Medicamento: {pacientes[i, 6]}")
                print("--------------------------------------------")
    elif opcion == 6:
        mostrar_posiciones_pacientes(pacientes, num_pacientes)
    elif opcion == 7:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida, reintente nuevamente.")

# Guardar la información del paciente en un archivo JSON
json_data = {
    "pacientes": [
        {
            "nombre": pacientes[i, 0],
            "rut": pacientes[i, 1],
            "edad": pacientes[i, 2],
            "sexo": pacientes[i, 3],
            "direccion": pacientes[i, 4],
            "diagnostico": pacientes[i, 5],
            "medicamento": pacientes[i, 6]
        }
        for i in range(num_pacientes)
    ]
}

with open("pacientes.json", "w") as archivo_json:
    json.dump(json_data, archivo_json, indent=4)

# Guardar la información del paciente en un archivo txt
with open("pacientes.txt", "w") as archivo_txt:
    for i in range(num_pacientes):
        archivo_txt.write(f"Nombre: {pacientes[i, 0]}\n")
        archivo_txt.write(f"RUT: {pacientes[i, 1]}\n")
        archivo_txt.write(f"Edad: {pacientes[i, 2]}\n")
        archivo_txt.write(f"Sexo: {pacientes[i, 3]}\n")
        archivo_txt.write(f"Dirección: {pacientes[i, 4]}\n")
        archivo_txt.write(f"Diagnóstico: {pacientes[i, 5]}\n")
        archivo_txt.write(f"Medicamento: {pacientes[i, 6]}\n")
        archivo_txt.write("----------------------------\n")

