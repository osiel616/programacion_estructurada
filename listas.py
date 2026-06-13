import os

# Ejemplo 1: Crear una lista de numeros e imprimir el contenido
numeros = [10, 34, 25, 45]

while opcion == "SI":
    numero = int(input("Dame un numero: "))
    numeros.append(numero)
    opcion = input("¿Deseas agregar otro numero? (SI/NO): ").upper().strip()
print(numeros)

# Ejemplo 2: Crear una lista de palabras y posteriormente buscar la 
# concidencia de una palabra
# 1er forma
palabras = ["UTD", "Segundo", "TI", "MTI"]
palabra = input("Dame la palabra a buscar: ").strip()

if palabra in palabras:
    print("Encontre la palabra en la lista")
else: 
    print("NO se encontro la palabra en la lista")

# Ejemplo 3: Añadir elementos a la lista
# 1er forma
lista = []

true = True
while true:
    dato = input("Ingrese un valor para la lista: ").strip().upper()
    lista.append(dato)
    true = input("¿Deseas añadir mas elementos a la lista? (Si/No)").lower().strip()

    if true == "No":
        true = False

# 2da forma
true = "Si"
while true == "Si":
    dato = input("Ingrese un valor a la lista: ").strip().upper()
    lista.append(dato)
    true = input("¿Deseas añadir mas elementos a la lista? (Si/No)").lower().strip()

print(lista)

# Ejemplo 4: Crear una lista multidimensional que permita almacenar el nombre y telefono
# de una agenda
agenda=[ 
    ["Carlos", "6181234567"],
    ["Alberto", "6182344567"],
    ["Martin", "6181231223"],
    ]
print(agenda)

for i in agenda:
    print(i)

for c in range(0,2):
    for r in range(0.3):
        print(agenda[r],[c])

lista = ""
for r in range(0,3):
    for c in range(0,2):
        lista += f"{agenda[r][c]}, "
    lista += "\n"
print("["+lista+"]")
